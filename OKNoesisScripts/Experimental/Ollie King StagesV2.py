# Ollie King Stages V2 script (Arcade)
# Noesis script by KC, 2023
# Last updated: 4 June 2023

# ** WORK IN PROGRESS! **


from inc_noesis import *

import binascii


def registerNoesisTypes():
    handle = noesis.register("Ollie King Stages 2 (Arcade)",".mdb")
    noesis.setHandlerTypeCheck(handle, bcCheckType)
    noesis.setHandlerLoadModel(handle, bcLoadModel)
    return 1


# Check file type

def bcCheckType(data):
    return 1


# Read the model data

def bcLoadModel(data, mdlList):

    mesh_num = 0
    firstTableSize = 0
    secondTablePtr = 0
    currPos = 0x100
    testForFormatString = False
    vert_count = 0
    face_count = 0
    vert_Stride_Value = None
    UV_Stride_Value = None
    Normals_Stride_Value = None
    hasNormals = False

    bs = NoeBitStream(data)
    ctx = rapi.rpgCreateContext()

    curr_folder = rapi.getDirForFilePath(rapi.getInputName()).lower()
    curr_file = rapi.getLocalFileName(rapi.getInputName()).lower()

    mesh_name = curr_file.replace(".mdb", "")
    noesis.logPopup()

    bs.seek(0x4)
    firstTableSize = bs.readUInt() # first, get the first table's size. Needed for second table.
    print('First table size: ' + str(firstTableSize))
    if firstTableSize == 0:
        return 1

    bs.seek(0x100)
    firstTablePtr = bs.readUInt() # check if there's a ptr to the first offset of second table
    print('First table ptr: ' + str(firstTablePtr))

    while firstTablePtr == 0:
        currPos += 0x80
        bs.seek(currPos) # if not, increment by 0x80 until we find it. TODO: solve situation where the second table doesn't really exist.
        print('CurrPos: ' + hex(currPos))
        firstTablePtr = bs.readUInt()
        print('ptr is: ' + hex(firstTablePtr))

    bs.seek(firstTablePtr) # goes to the first entry in the second table if read properly
    temp = bs.readUInt()
    print('First entry second table: ' + hex(temp))

    # Go down the second table and search for the format string at the end of it
    while testForFormatString != True:
        firstTablePtr += (0x20)
        bs.seek(firstTablePtr + 0x8)
        formatString = bs.readUInt()
        if formatString == 0x0142 or formatString == 0x0242 or formatString == 0x0112 or formatString == 0x0212:
            print('CurrPos: ' + hex(firstTablePtr))
            bs.seek(firstTablePtr)
            vert_count = bs.readUInt()
            print('Vert Count: ' + str(vert_count))
            face_count = bs.readUInt()
            print('Face Count: ' + str(face_count))
            testForFormatString = True
            print('Format string found: ' + hex(formatString))

            # Depending on stage type, change vertex padding/stride. Noesis gets mad when switch cases show up so if-elif used ugh
            if formatString == 0x0142:
                vert_Stride_Value = 0x12
                UV_Stride_Value = 0x16
                hasNormals = False
                #Normals start at vert_offset + 0xc
                #UVs start at vert_offset + 0x18
            elif formatString == 0x0242:
                vert_Stride_Value = 0x20
                UV_Stride_Value = 0x24
                hasNormals = False
                #Normalss start at vert_offset + 0xc
                #UVs start at vert_offset + 0x18
            elif formatString == 0x0112:
                vert_Stride_Value = 0x20
                Normals_Stride_Value = 0x20
                UV_Stride_Value = 0x24
                hasNormals = True
                #Normals start at vert_offset + 0xc
                #UVs start at vert_offset + 0x18
            elif formatString == 0x0212:
                vert_Stride_Value = 0x28
                Normals_Stride_Value = 0x28
                UV_Stride_Value = 0x32
                hasNormals = True

    firstTablePtr += 0x20 # increments to the start of the first mesh
    bs.seek(firstTablePtr)
    print('CurrPos: ' + hex(firstTablePtr))
    meshStart = firstTablePtr

    vertices = bytes()
    vertices = bs.readBytes(vert_count * vert_Stride_Value) # reads in the first mesh so far. Reads in the faces after readjusting the offset with the below loop
    # vertList = bytearray(list(vertices))
    # # print(str(vertList))
    # print(", ".join(hex(b) for b in vertList))

    vertCurrCount = 0
    vertTrackList = bytes()
    bs.seek(meshStart)
    print('CurrPos: ' + hex(meshStart))
    for v in range (vert_count*2):
        vx, vy, vz = bs.read("3f")
        vertTrackList += noePack("3f", vx, vy, vz) # reads the pos and appends to verts bytes obj
    
    # After we incremented with this loop for tracking, we can now read faces and repeat (we are at the faces of the first mesh)
    faces = bs.readBytes(face_count * 2)
    print(binascii.hexlify(faces))

    rapi.rpgSetName(mesh_name + "_" + str(mesh_num))
    rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, vert_Stride_Value, 0)
    rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, face_count, noesis.RPGEO_TRIANGLE_STRIP)

    try:
        mdl = rapi.rpgConstructModel()
        print("Worked")
    except:
        mdl = NoeModel()
        print("Didn't work")

    mdlList.append(mdl)

    return 1

# NOTE: modularize the above into separate functions we can call instead of being wonky with loops
# def tableSearch():
# def meshParse():
# def faceParse():

    

    

