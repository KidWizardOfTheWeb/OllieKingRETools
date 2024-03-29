# Ollie King Stages script (Arcade)
# Noesis script by KC, 2022
# Last updated: 10 August 2022

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

    # Changed to manual file choosing for testing, removed functionality until texture IDs are found
    txb_file = rapi.loadPairedFileGetPath("texture file", ".txb")
    while(txb_file):
        tex_file = NoeBitStream(rapi.loadIntoByteArray(txb_file[1]))
        mat_list, tex_list = ReadTextures(tex_file)
        txb_file = rapi.loadPairedFileGetPath("texture file file", ".txb")
    # print("Proceeding to mesh parsing...") # Once complete, display message before attempting to find entry point.

    meshInfoStart = noesis.userPrompt(noesis.NOEUSERVAL_INT, "Mesh info starting address entry", "Enter the address where the mesh info starts at (about 0x20 before actual mesh start).", "0x0")
    faceStart = noesis.userPrompt(noesis.NOEUSERVAL_INT, "Face info starting address entry", "Enter the address where the face info starts at (after mesh end).", "0x0")
    primPrompt = noesis.userPrompt(noesis.NOEUSERVAL_INT, "Primitive type entry", "Enter 0 for triangle primatives, or enter 1 for tristrip primatives.", "0")

    bs.seek(meshInfoStart) # Changed seek to manual input for current usage
    vert_offset = meshInfoStart + 0x20
    print("Vert offset: " + hex(vert_offset))
    vert_count = bs.readUInt()
    print("Vert count: " + str(vert_count))
    face_count = bs.readUInt()
    print("Face count: " + str(face_count))
    stage_type = bs.readUInt()
    print("Stage type: " + hex(stage_type))
    extra_info = bs.readUInt()
    print("Extra info: " + hex(extra_info))

    vert_Stride_Value = None
    # Depending on stage type, change vertex padding/stride.
    if stage_type == 0x0142:
        vert_Stride_Value = 0x12
        UV_Stride_Value = 0x16
        hasNormals = False
        #Normals start at vert_offset + 0xc
        #UVs start at vert_offset + 0x18
    elif stage_type == 0x0242:
        vert_Stride_Value = 0x20
        UV_Stride_Value = 0x24
        hasNormals = False
        #Normalss start at vert_offset + 0xc
        #UVs start at vert_offset + 0x18
    elif stage_type == 0x0112:
        vert_Stride_Value = 0x20
        Normals_Stride_Value = 0x20
        UV_Stride_Value = 0x24
        hasNormals = True
        #Normals start at vert_offset + 0xc
        #UVs start at vert_offset + 0x18
    elif stage_type == 0x0212:
        vert_Stride_Value = 0x28
        Normals_Stride_Value = 0x28
        UV_Stride_Value = 0x32
        hasNormals = True
        #Normals start at vert_offset + 0xc
        #UVs start at vert_offset + 0x18
    print("Vertex stride value: " + str(vert_Stride_Value))
    # table2 = bs.readUInt()
    # table2_size = bs.readUInt()
    # table1 = bs.readUInt()
    # entries = bs.readUInt()

    # print(table2) # Table sometimes gets populated, print some info on it.
    # print("Entries: " + str(entries)) # No entries happen, which mean loop never starts.
    
    # print("Loop starts after here.") # Another confirmation because I just gotta know.
    # for a in range(entries): loop removed currently
    # print("Now we're in it.") # And another confirmation because I need to know when I'm in the loop. Haven't gotten in, yet.
    # bs.seek(table2 + (a * 0x20))
    # print(bs.seek(table2 + (a * 0x20)))
    bs.seek(vert_offset)
    # offset = bs.readUInt() + 0x20
    # print(offset)
    # offset2 = bs.readUInt() + 0x20
    # tex_num = bs.readUInt()
    # bs.seek(offset)
    # prim_type = bs.readUInt()							# 4 = triangles, 5 = strips
    # entry_type = bs.readUInt()

    # print("Entry type not found (yet).")
    # if entry_type == 0x0142:							# mesh info, stride 0x28, changed to user input for the time being. Input the offset where vert_count, face_count, and mesh type is found.
        # print("Entry type found.")
        # vert_offset = meshInfoStart + 0x20
        # vert_count = bs.readUInt()
        # face_offset = faceStart
        # face_count = bs.readUInt()

        # bs.seek(vert_offset) # vert offset determined by user input
    vertices = bytes()
    vertices = bs.readBytes(vert_count * vert_Stride_Value)
    # vertList = bytearray(list(vertices))
    # print(str(vertList))
    # print(", ".join(hex(b) for b in vertList))

    if hasNormals:
        # Normals reading
        bs.seek(vert_offset + 0xc)
        # <- replace 0xc with value designated by stage type
        normals = bytes()
        normals = bs.readBytes(vert_count * Normals_Stride_Value)
        # normalsList = bytearray(list(normals))
        # print(", ".join(hex(b) for b in normalsList))

    # UVs reading
    bs.seek(vert_offset + 0x18)
    #  <- replace 0x18 with value designated by stage type
    UV = bytes()
    UV = bs.readBytes(vert_count * UV_Stride_Value)
    # UVsList = bytearray(list(UV))
    # print(", ".join(hex(b) for b in UVsList))


    # for v in range(vert_count):
    #     vx, vy, vz = bs.read("3f")
    #     unk1 = bs.read("1f")
    #     # vx, vy, vz, unk1 = bs.read("4f")
    #     print("Vertex " + str(v+1) + ": " + str(vx) + ", " + str(vy) + ", " + str(vz))
    #     # print("Vertex " + str(v) + ": " + str(vx) + ", " + str(vy) + ", " + str(vz) + ", " + str(unk1))
    #     if stage_type == 0x0142:
    #         pad1 = bs.readUInt64()
    #         pad2 = bs.readFloat()
    #         # print ("Pad " + str(v+1) + ": "+ str(pad1) + ", " + str(pad2))
    #     elif stage_type == 0x0242:
    #         pad1 = bs.readUInt64()
    #         pad2 = bs.readUInt64()
    #         # print ("Pad " + str(v+1) + ": "+ str(pad1) + ", " + str(pad2))
    #     elif stage_type == 0x0112:
    #         pad1 = bs.readUInt64()
    #         pad2 = bs.readUInt64()
    #         # print ("Pad " + str(v+1) + ": "+ str(pad1) + ", " + str(pad2))
    #     elif stage_type == 0x0212:
    #         pad1 = bs.readUInt64()
    #         pad2 = bs.readUInt64()
    #         pad3 = bs.readUInt64()
    #         pad4 = bs.readFloat()
    #         # print ("Pad " + str(v+1) + ": "+ str(pad1) + ", " + str(pad2) + ", " + str(pad3) + ", " + str(pad4))
    #     # vx, vy, vz = bs.read("3f")
    #     # b_idx = bs.read("I")[0]
    #     # nx, ny, nz = bs.read("3f")
    #     # uvx, uvy = bs.read("2f")
    #     # vz = vz
    #     vertices += noePack("3f", vx, vy, vz)
    # #     # vertices += noePack("ffffIfffff", vx, vy, vz, unk1, b_idx, nx, ny, nz, uvx, uvy)
    # #     # print(noeUnpack("f", vertices))
    bs.seek(faceStart) # face offset determined by user input
    faces = bs.readBytes(face_count * 2)

    rapi.rpgSetName(mesh_name + "_" + str(mesh_num))
    rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, vert_Stride_Value, 0)
    if hasNormals:
        rapi.rpgBindNormalBufferOfs(normals, noesis.RPGEODATA_FLOAT, Normals_Stride_Value, 0)
        rapi.rpgBindUV1BufferOfs(UV, noesis.RPGEODATA_FLOAT, UV_Stride_Value, 0)
    else:
        rapi.rpgBindNormalBufferOfs(None, noesis.RPGEODATA_FLOAT, Normals_Stride_Value, 0)
        rapi.rpgBindUV1BufferOfs(UV, noesis.RPGEODATA_FLOAT, UV_Stride_Value, 0)
    # rapi.rpgSetMaterial("Material_" + str(tex_num))
    # rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, 0x28, 0)
    # # rapi.rpgBindBoneIndexBufferOfs(vertices, noesis.RPGEODATA_UBYTE, 0x28, 0x10, 4)
    # rapi.rpgBindNormalBufferOfs(vertices, noesis.RPGEODATA_FLOAT, 0x28, 0x14)
    # rapi.rpgBindUV1BufferOfs(vertices, noesis.RPGEODATA_FLOAT, 0x28, 0x20)

    if primPrompt == 0:
        rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE)

        mesh_num += 1

    if primPrompt == 1:
        rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE_STRIP)

        mesh_num += 1

    # if prim_type == 4:
    #     rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE)

    # if prim_type == 5:
    #     rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE_STRIP)

    #     mesh_num += 1

    # else:
    #     print("Unknown entry type: ", hex(entry_type))


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

        curr_file = rapi.getLocalFileName(rapi.getInputName()).lower()

        if img_type == 7:
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT1)

        elif img_type == 8:
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT5)

        elif img_type == 1:
            raw_image = rapi.imageDecodeRaw(raw_image, width, width, "b5g5r5p1")
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        elif img_type == 4:
            # What is this lmfao.
            print("Image type: ", img_type, "at ", hex(offset), "Image number: ", str(a))					
            raw_image = rapi.imageDecodeRaw(raw_image, width, width, "b4g4r4a4")
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        elif img_type == 9: # Similar to 8, listed as different image type
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT5)

        elif img_type == 6: # Used for first image of s3_tenkyu and obi. They are different formats however, so edgecase is used.
            if curr_file == "obi.txb":
                raw_image = rapi.imageDecodeRaw(raw_image, width, width, "r8g8b8a8")
                tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)
            else:
                raw_image = rapi.imageFromMortonOrder(raw_image, width, width)
                tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        elif img_type == 3: # Xbox Morton order.
            # TODO: Confirm if this is the proper DXT format. 
            raw_image = rapi.imageFromMortonOrder(raw_image, width, width)
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT5)

        elif img_type == 5: # Xbox Morton order.
        # Used in London stages and Kyoto skyboxes: s2_area16.txb, s5_area02.txb, s5_area18.txb, s3_tenkyu.txb, s6_tenkyu.txb
            raw_image = rapi.imageFromMortonOrder(raw_image, width, width)
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        else:
            print("Unknown image type: ", img_type, "at ", hex(offset))


        tex_list.append(tex1)
        material.setTexture("Texture_" + str(a))
        mat_list.append(material)

        offset += data_size + 0x20

    return mat_list, tex_list
