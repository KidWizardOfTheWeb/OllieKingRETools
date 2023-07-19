# Ollie King Stages V2 script (Arcade)
# Noesis script by KC, 2023
# Last updated: 19 July 2023

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
    # currPos = 0x100
    vert_count = 0
    formatLength = 0
    faceDataArray = None

    global bs # we operate the bit stream constantly so its gotta be global
    bs = NoeBitStream(data)
    ctx = rapi.rpgCreateContext()

    curr_folder = rapi.getDirForFilePath(rapi.getInputName()).lower()
    curr_file = rapi.getLocalFileName(rapi.getInputName()).lower()

    mesh_name = curr_file.replace(".mdb", "")
    noesis.logPopup()

    firstTablePtr, faceDataArray = firstTableSearch() # Beginning of file reading is in here, gets us to the first line and reads it
    # firstTableSubmeshInfo()

    meshInfo, firstTablePtr = formatDataSearch(firstTablePtr)

    firstTablePtr += 0x20 # increments to the start of the first mesh
    bs.seek(firstTablePtr)
    print('CurrPos (should be at first mesh here): ' + hex(firstTablePtr))
    meshStart = firstTablePtr

    vertices = meshParse(meshInfo, meshStart) # should return vertices

    faceParse(meshInfo, faceDataArray, vertices, mesh_name) # should return faces
    
    # After we incremented with this loop for tracking, we can now read faces and repeat (we are at the faces of the first mesh)
    # faces = bs.readBytes(meshInfo["faceCount"] * 2)
    # print(binascii.hexlify(faces))

    # rapi.rpgSetName(mesh_name + "_" + str(mesh_num))
    # rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, meshInfo["vertStride"], 0)

    # # TODO: figure out what determines primitive type

    # if meshInfo["formatLength"] == 24:
    #     try:
    #         rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, meshInfo["faceCount"], noesis.RPGEO_TRIANGLE_STRIP)
    #         print("Tri-Strip(?) prim type model found.")
    #     except:
    #         rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, meshInfo["faceCount"], noesis.RPGEO_TRIANGLE)
    #         print("Triangles(?) prim type model found.")
    #     mesh_num += 1
    # elif meshInfo["formatLength"] == 32:
    #     try:
    #         rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, meshInfo["faceCount"], noesis.RPGEO_TRIANGLE_STRIP)
    #         print("Tri-Strip(?) prim type model found.")
    #     except:
    #         rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, meshInfo["faceCount"], noesis.RPGEO_TRIANGLE)
    #         print("Triangles(?) prim type model found.")
    #     mesh_num += 1
    # elif meshInfo["formatLength"] == 40:
    #     try:
    #         rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, meshInfo["faceCount"], noesis.RPGEO_TRIANGLE_STRIP)
    #         print("Tri-Strip(?) prim type model found.")
    #     except:
    #         rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, meshInfo["faceCount"], noesis.RPGEO_TRIANGLE)
    #         print("Triangles(?) prim type model found.")
    #     mesh_num += 1

    try:
        mdl = rapi.rpgConstructModel()
        print("Worked")
    except:
        mdl = NoeModel()
        print("Didn't work")

    mdlList.append(mdl)

    return 1

"""
def firstTableSubmeshInfo():
    submeshFaceCounts = [0]
    bs.seek(0x98) # This is usually where the first table entry is.
    tableEntryNum = bs.readUInt()
    if tableEntryNum != 1:
        return 1
    
    bs.seek(0xD4) # first entry's important data starts here



"""

def firstTableSearch():
    # currPos = 0x100
    bs.seek(0x4)
    firstTableSize = bs.readUInt() # first, get the first table's size. Needed for second table.
    print('First table size: ' + str(firstTableSize))
    if firstTableSize == 0:
        return 1

    # each entry here includes face data values for each section.
    # first, create an array to store face data length, group ID, and tri-type
    faceDataLengths = [[0 for i in range (3)] for j in range (firstTableSize)]
    currPos = 0xD4 # all files start at D4, jump to this offset
    bs.seek(currPos)
    for i in range (firstTableSize - 1):
        faceDataLengths[i][0] = bs.readUInt()
        bs.seek(currPos + 0xC)
        faceDataLengths[i][2] = bs.readInt()
        print('face data length and tri-type: ' + str(faceDataLengths[i]))
        currPos += 0x80
        bs.seek(currPos)
        
    currPos -= 0x40 # move back due to final iteration of previous loop being ahead and record group IDs with this mini table
    bs.seek(currPos)
    for i in range (firstTableSize - 1):
        faceDataLengths[i][1] = bs.readUInt()
        print('face data group ID: ' + str(faceDataLengths[i]))

    for i in range (len(faceDataLengths)):
        for j in range(0, len(faceDataLengths) - i - 1):
            if faceDataLengths[j][1] > faceDataLengths[j+1][1]:
                temp = faceDataLengths[j]
                faceDataLengths[j] = faceDataLengths[j+1]
                faceDataLengths[j+1] = temp

    faceDataLengths.remove([0, 0, 0]) # TODO: find out why another entry is generated with the bubble sort above
    for i in range (len(faceDataLengths)):
        if faceDataLengths[i][2] == -1:
            pass
        elif faceDataLengths[i][2] == -2:
            faceDataLengths[i][0] += 2
        print('sort list: ' + str(faceDataLengths[i]))

    # use the above data for face reading, return to main body

    currPos = 0x100
    bs.seek(0x70) # jump to what points to what would be the possible ptr to the first offset of second table
    firstTableEntry = bs.readInt()
    print('First table entry: ' + str(hex(firstTableEntry)))

    bs.seek(firstTableEntry)

    firstTablePtr = bs.readUInt() # check if there's a ptr to the first offset of second table
    print('First table ptr: ' + str(hex(firstTablePtr)))

    while firstTablePtr == 0:
        currPos += 0x80
        bs.seek(currPos) # if not, increment by 0x80 until we find it. TODO: solve situation where the second table doesn't really exist.
        print('CurrPos: ' + hex(currPos))
        firstTablePtr = bs.readUInt()
        print('ptr is: ' + hex(firstTablePtr))

    bs.seek(firstTablePtr) # goes to the first entry in the second table if read properly
    temp = bs.readUInt()
    print('First entry second table: ' + hex(temp))
    return firstTablePtr, faceDataLengths

def formatDataSearch(firstTablePtr):
    # Go down the second table and search for the format string at the end of it
    testForFormatString = False
    face_count = 0
    vert_Stride_Value = None
    UV_Stride_Value = None
    Normals_Stride_Value = None
    hasNormals = False
    testForFormatString = False
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
            bs.seek(firstTablePtr + 0xC)
            formatLength = bs.readUInt()
            print('Prim type: ' + str(formatLength))
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
            
            # dictionary is much easier to handle. Also pass back table ptr for scan operation to continue.
            meshInfo = {
                "vertCount": vert_count,
                "faceCount": face_count,
                "formatString": formatString,
                "formatLength": formatLength,
                "vertStride": vert_Stride_Value,
                "normalStride": Normals_Stride_Value,
                "uvStride": UV_Stride_Value,
                "normals": bool(hasNormals)
            }

            return meshInfo, firstTablePtr

def meshParse(meshInfo, meshStart):
    vertTrackOffset = meshStart
    vertices = bytes()
    vertices = bs.readBytes(meshInfo["vertCount"] * meshInfo["vertStride"]) # reads in the first mesh so far. Reads in the faces after readjusting the offset with the below loop
    # vertList = bytearray(list(vertices))
    # # print(str(vertList))
    # print(", ".join(hex(b) for b in vertList))

    # vertCurrCount = 0
    vertTrackList = bytes()
    bs.seek(meshStart)
    print('CurrPos (should be back to first position of first mesh after reading bytes here): ' + hex(meshStart))
    if meshInfo["formatString"] == 0x0142:
        # 3 floats of padding
        for v in range (meshInfo["vertCount"]*2):
            vx, vy, vz = bs.read("3f")
            vertTrackList += noePack("3f", vx, vy, vz) # reads the pos and appends to verts bytes obj
    elif meshInfo["formatString"] == 0x0242:
        for v in range (meshInfo["vertCount"]):
            vx, vy, vz = bs.read("3f")
            vertTrackList += noePack("3f", vx, vy, vz) # reads the pos and appends to verts bytes obj
            vertTrackOffset += 0x20
            bs.seek(vertTrackOffset)
    elif meshInfo["formatString"] == 0x0112:
        for v in range (meshInfo["vertCount"]):
            vx, vy, vz = bs.read("3f")
            vertTrackList += noePack("3f", vx, vy, vz) # reads the pos and appends to verts bytes obj
            vertTrackOffset += 0x20
            bs.seek(vertTrackOffset)
    elif meshInfo["formatString"] == 0x0212:
        for v in range (meshInfo["vertCount"]):
            vx, vy, vz = bs.read("3f")
            vertTrackList += noePack("3f", vx, vy, vz) # reads the pos and appends to verts bytes obj
            vertTrackOffset += 0x28
            bs.seek(vertTrackOffset)

    return vertices

def faceParse(meshInfo, faceDataArray, vertices, mesh_name):
    print("Current offset for face values: "+ hex(bs.getOffset()))

    i = 0
    mesh_num = 0
    while faceDataArray[i][1] == 0:
        print('Current face data array: ' + str(faceDataArray[i]))
        if faceDataArray[i][2] == -1:
            faces = bs.readBytes(faceDataArray[i][0] * 6)
            print("Current offset for after face values: "+ hex(bs.getOffset()))

            rapi.rpgSetName(mesh_name + "_" + str(mesh_num))
            rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, meshInfo["vertStride"], 0)

            rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, faceDataArray[i][0] * 3, noesis.RPGEO_TRIANGLE)
            print("Triangles prim type model found.")
            print("Current offset for after face values: "+ hex(bs.getOffset()))
        elif faceDataArray[i][2] == -2:
            faces = bs.readBytes(faceDataArray[i][0] * 2)

            rapi.rpgSetName(mesh_name + "_" + str(mesh_num))
            rapi.rpgBindPositionBufferOfs(vertices, noesis.RPGEODATA_FLOAT, meshInfo["vertStride"], 0)

            rapi.rpgCommitTriangles(faces, noesis.RPGEODATA_USHORT, faceDataArray[i][0], noesis.RPGEO_TRIANGLE_STRIP)
            print("Tri-Strip prim type model found.")
            print("Current offset for after face values: "+ hex(bs.getOffset()))
        i += 1
        mesh_num += 1

        print("Current offset for pre calculation regulation: "+ hex(bs.getOffset()))
        # bs.getOffset() // 10**0 % 10
        if (bs.getOffset() % 16 != 0):
            offsetRemainder = 16 - (bs.getOffset() % 16)
            print('offset remainder: ' + hex(offsetRemainder))
            offsetAdjust = bs.getOffset() + offsetRemainder
            
            # offsetAdjust += 0x10
            print('offset adjust: ' + hex(offsetAdjust))
            bs.seek(offsetAdjust)
        print("Current offset for post calculation regulation: "+ hex(bs.getOffset()))

    

    # faces = bs.readBytes(meshInfo["faceCount"] * 2)
    # print("Current offset for after face values: "+ hex(bs.getOffset()))
    # return faces
