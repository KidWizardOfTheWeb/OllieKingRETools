# Ollie King (Arcade)
# Noesis script by KC, 2022
# Last updated: 25 June 2022

# ** WORK IN PROGRESS! **


from inc_noesis import *


def registerNoesisTypes():
    handle = noesis.register("Ollie King Stages (Arcade)",".mdb")
    noesis.setHandlerTypeCheck(handle, bcCheckType)
    noesis.setHandlerLoadModel(handle, bcLoadModel)
    return 1


# Check file type

def bcCheckType(data):
    return 1


# Read the model data

def bcLoadModel(data, mdlList):
    bs = NoeBitStream(data)
    ctx = rapi.rpgCreateContext()

    curr_folder = rapi.getDirForFilePath(rapi.getInputName()).lower()
    curr_file = rapi.getLocalFileName(rapi.getInputName()).lower()

    mesh_name = curr_file.replace(".mdb", "")
    # txb_file = curr_folder + mesh_name + ".txb"
    mesh_num = 0

    # Changed to manual file choosing for testing
    txb_file = rapi.loadPairedFileGetPath("texture file", ".txb")
    while(txb_file):
        tex_file = NoeBitStream(rapi.loadIntoByteArray(txb_file[1]))
        mat_list, tex_list = ReadTextures(tex_file)
        txb_file = rapi.loadPairedFileGetPath("texture file file", ".txb")
    print("Proceeding to mesh parsing...") # Once complete, display message before attempting to find entry point.


    # bones = []
    # bone_num = 0

    # parent_info = [-1, 0, 1, 2, 3, 4, 4, 6, 7, 8, 4, 10, 11, 12, 1, 14, 15, 1, 17, 18, 0]				# default parent info for all skeletons, unneeded

    bs.seek(8) # TODO: figure out where to find the entry point by changing this to seek somewhere else.
    print(bs.seek(8))
    table2 = bs.readUInt() + 0x20
    table2_size = bs.readUInt()
    table1 = bs.readUInt()
    entries = bs.readUInt()

    print(table2 - 0x20) # Table sometimes gets populated, print some info on it.
    print("Entries: " + str(entries)) # No entries happen, which mean loop never starts.
    
    print("Loop starts after here.") # Another confirmation because I just gotta know.
    for a in range(entries):
        print("Now we're in it.") # And another confirmation because I need to know when I'm in the loop. Haven't gotten in, yet.
        bs.seek(table2 + (a * 0x20))
        offset = bs.readUInt() + 0x20
        offset2 = bs.readUInt() + 0x20
        tex_num = bs.readUInt()
        bs.seek(offset)
        prim_type = bs.readUInt()							# 4 = triangles, 5 = strips
        entry_type = bs.readUInt()

        # if entry_type == 0x112:							# bone info, don't need it and will remove later.
        #     bs.seek(offset + 0x20)
        #     pos = NoeVec3.fromBytes(bs.readBytes(12))
        #     matrix = NoeAngles([0,0,90]).toMat43()
        #     pos[2] *= -1 # had to add this recently, something changed with the script and it didn't automatically fix it anymore so this properly flips Z coords of bone position to be on the mesh
        #     matrix[3] = pos
        #     bones.append(NoeBone(bone_num, "Bone_" + str(bone_num), matrix, None, parent_info[bone_num]))
        #     bone_num += 1
        print("Entry type not found (yet).")
        if entry_type == 0x142:							# mesh info, stride 0x28, hardcoded one entry type of 42 01 00 00 so far.
            print("Entry type found.")
            vert_offset = bs.readUInt() + 0x20
            vert_count = bs.readUInt()
            face_offset = bs.readUInt() + 0x20
            face_count = bs.readUInt()

            bs.seek(vert_offset)
            vertices = bytes()

            for v in range(vert_count):
                vx, vy, vz, unk1 = bs.read("4f")
                b_idx = bs.read("I")[0]
                nx, ny, nz = bs.read("3f")
                uvx, uvy = bs.read("2f")
                vz = -vz
                vertices += noePack("ffffIfffff", vx, vy, vz, unk1, b_idx, nx, ny, nz, uvx, uvy)

            bs.seek(face_offset)
            faces = bs.readBytes(face_count * 2)

            rapi.rpgSetName(mesh_name + "_" + str(mesh_num))
            rapi.rpgSetMaterial("Material_" + str(tex_num))
            rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, 0x28, 0)
            rapi.rpgBindBoneIndexBufferOfs(vertices, noesis.RPGEODATA_UBYTE, 0x28, 0x10, 4)
            rapi.rpgBindNormalBufferOfs(vertices, noesis.RPGEODATA_FLOAT, 0x28, 0x14)
            rapi.rpgBindUV1BufferOfs(vertices, noesis.RPGEODATA_FLOAT, 0x28, 0x20)

            if prim_type == 4:
                rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE)

            if prim_type == 5:
                rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE_STRIP)

            mesh_num += 1

        else:
            print("Unknown entry type: ", hex(entry_type))


    try:
        mdl = rapi.rpgConstructModel()
    except:
        mdl = NoeModel()

    mdl.setModelMaterials(NoeModelMaterials(tex_list, mat_list))
    # mdl.setBones(bones)
    mdlList.append(mdl)

    return 1


def ReadTextures(bs):
    mat_list = []
    tex_list = []

    bs.seek(4)
    tex_count = bs.readUInt()
    print("Tex count: ", tex_count)

    offset = 0x20

    for a in range(tex_count):
        material = NoeMaterial("Material_" + str(a), "")
        bs.seek(offset)
        data_size = bs.readUInt()
        width = bs.readUInt()
        bs.seek(offset + 0xc)
        img_type = bs.readUInt()

        bs.seek(offset + 0x20)
        raw_image = bs.readBytes(data_size)

        if img_type == 7:
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT1)

        elif img_type == 8:
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT5)

        elif img_type == 1:
            raw_image = rapi.imageDecodeRaw(raw_image, width, width, "b5g5r5p1")
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        elif img_type == 4:										# same as type 1 ?
            raw_image = rapi.imageDecodeRaw(raw_image, width, width, "b5g5r5p1")
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        else:
            print("Unknown image type: ", img_type, "at ", hex(offset))


        tex_list.append(tex1)
        material.setTexture("Texture_" + str(a))
        mat_list.append(material)

        offset += data_size + 0x20

    return mat_list, tex_list