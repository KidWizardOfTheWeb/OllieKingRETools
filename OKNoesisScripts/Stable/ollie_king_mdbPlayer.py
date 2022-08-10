# Ollie King (Arcade)
# Noesis script by KC 2022
# Last updated: 10 August 2022

# ** WORK IN PROGRESS! **


from inc_noesis import *
animNames = ["A_air_000", "A_air_001", "A_air_002", "A_air_002_B", "A_air_002_F", "A_air_002_L", "A_air_002_R", "A_air_010", "A_air_011", "A_air_012", "A_air_012_B", "A_air_012_F", "A_air_012_L", "A_air_012_R", "A_air_020", "A_air_021", "A_air_022", "A_air_030", "A_air_032", "A_air_040", "A_air_040_a", "A_air_040_b", "A_air_040_c", "A_air_040_s", "A_air_041", "A_air_042", "A_air_042_B", "A_air_042_F", "A_air_042_L", "A_air_042_R", "A_air_050", "A_air_052", "A_air_060", "A_air_062", "A_air_070", "A_air_072", "A_air_080", "A_air_080_a", "A_air_080_b", "A_air_080_c", "A_air_080_s", "A_air_081", "A_air_082", "A_air_082_B", "A_air_082_F", "A_air_082_L", "A_air_082_R", "A_air_090", "A_air_090_", "A_air_091", "A_air_092", "A_air_100", "A_air_101", "A_air_102", "A_air_110", "A_air_111", "A_air_112", "A_air_120", "A_air_122", "A_air_140", "A_air_141", "A_air_142", "A_air_R000", "A_air_R001", "A_air_R002", "A_air_R002_B", "A_air_R002_F", "A_air_R002_L", "A_air_R002_R", "A_air_R010", "A_air_R011", "A_air_R012", "A_air_R020", "A_air_R021", "A_air_R022", "A_air_R022_B", "A_air_R022_F", "A_air_R022_L", "A_air_R022_R", "A_air_R030", "A_air_R032", "A_air_R040", "A_air_R042", "A_air_R050", "A_air_R051", "A_air_R052", "A_air_R052_B", "A_air_R052_F", "A_air_R052_L", "A_air_R052_R", "A_air_R060", "A_air_R062", "A_air_R070", "A_air_R071", "A_air_R072", "A_air_R072_B", "A_air_R072_F", "A_air_R072_L", "A_air_R072_R", "A_air_R080", "A_air_R081", "A_air_R082", "A_air_R082_B", "A_air_R082_F", "A_air_R082_L", "A_air_R082_R", "A_air_R090", "A_air_R091", "A_air_R092", "A_air_R100", "A_air_R102", "A_air_R110", "A_air_R112", "A_air_R120", "A_air_R122", "A_air_R130", "A_air_R132", "A_air_R180", "A_air_R181", "A_air_R182", "A_air_R182_B", "A_air_R182_F", "A_air_R182_L", "A_air_R182_R", "A_air_V000", "A_air_V002", "A_air_V030", "A_air_V031", "A_air_V032", "A_air_V040", "A_air_V042", "A_air_V050", "A_air_V051", "A_air_V052", "A_air_V052_B", "A_air_V052_F", "A_air_V052_L", "A_air_V052_R", "A_air_V060", "A_air_V061", "A_air_V062", "A_air_V070", "A_air_V072", "A_air_V080", "A_air_V081", "A_air_V082", "A_air_V090", "A_air_V092", "A_air_V100", "A_air_V102", "A_air_V120", "A_air_V122", "A_air_V130", "A_air_V132", "A_air_V140", "A_air_V142", "A_air_V150", "A_air_V151", "A_air_V152", "A_air_V160", "A_air_V162", "A_air_V170", "A_air_V172", "A_attack_kick_L01", "A_attack_kick_R01", "A_attack_L01", "A_attack_R01", "A_Crv_L01", "A_Crv_L01_boko", "A_Crv_L02", "A_Crv_L02_boko", "A_Crv_R01", "A_Crv_R01_boko", "A_Crv_R02", "A_Crv_R02_boko", "A_dwcrv_L", "A_Gap_ole", "A_Gap_ole01", "A_Grind_000", "A_Grind_00a", "A_Grind_001", "A_Grind_01a", "A_Grind_002", "A_Grind_02a", "A_Grind_003", "A_Grind_03a", "A_Grind_004", "A_Grind_04a", "A_Grind_005", "A_Grind_05a", "A_Grind_006", "A_Grind_06a", "A_Grind_007", "A_Grind_07a", "A_Grind_008", "A_Grind_08a", "A_Grind_009", "A_Grind_09a", "A_Grind_010", "A_Grind_10a", "A_Grind_011", "A_Grind_11a", "A_Grind_012", "A_Grind_12a", "A_Grind_013", "A_Grind_13a", "A_Grind_014", "A_Grind_14a", "A_Grind_015", "A_Grind_15a", "A_Grind_016", "A_Grind_16a", "A_Grind_017", "A_Grind_17a", "A_Grind_018", "A_Grind_019", "A_Grind_020", "A_Grind_021", "A_Grind_022", "A_Grind_023", "A_Grind_024", "A_Grind_025", "A_Grind_026", "A_Grind_027", "A_Grind_030", "A_Grind_031", "A_Grind_032", "A_Grind_033", "A_Grind_034", "A_Grind_035", "A_Grind_036", "A_Grind_037", "A_Grind_040", "A_Grind_041", "A_Grind_042", "A_Grind_043", "A_Grind_044", "A_Grind_045", "A_Grind_046", "A_Grind_047", "A_Grind_050", "A_Grind_051", "A_Grind_052", "A_Grind_053", "A_Grind_054", "A_Grind_055", "A_Grind_056", "A_Grind_057", "A_Grind_060", "A_Grind_061", "A_Grind_062", "A_Grind_063", "A_Grind_064", "A_Grind_065", "A_Grind_066", "A_Grind_067", "A_Grind_070", "A_Grind_071", "A_Grind_072", "A_Grind_073", "A_Grind_074", "A_Grind_075", "A_Grind_076", "A_Grind_077", "A_Grind_080", "A_Grind_081", "A_Grind_082", "A_Grind_083", "A_Grind_084", "A_Grind_085", "A_Grind_086", "A_Grind_087", "A_Grind_090", "A_Grind_091", "A_Grind_092", "A_Grind_093", "A_Grind_094", "A_Grind_095", "A_Grind_096", "A_Grind_097", "A_Grind_100", "A_Grind_101", "A_Grind_102", "A_Grind_103", "A_Grind_104", "A_Grind_105", "A_Grind_106", "A_Grind_107", "A_Grind_108", "A_Grind_109", "A_Grind_110", "A_Grind_111", "A_Grind_112", "A_Grind_113", "A_Grind_114", "A_Grind_115", "A_Grind_116", "A_Grind_117", "A_Grind_120", "A_Grind_121", "A_Grind_122", "A_Grind_123", "A_Grind_124", "A_Grind_125", "A_Grind_126", "A_Grind_127", "A_Grind_130", "A_Grind_131", "A_Grind_132", "A_Grind_133", "A_Grind_134", "A_Grind_135", "A_Grind_136", "A_Grind_137", "A_Grind_140", "A_Grind_141", "A_Grind_142", "A_Grind_143", "A_Grind_144", "A_Grind_145", "A_Grind_146", "A_Grind_147", "A_Grind_150", "A_Grind_151", "A_Grind_152", "A_Grind_153", "A_Grind_154", "A_Grind_155", "A_Grind_156", "A_Grind_157", "A_Grind_160", "A_Grind_161", "A_Grind_162", "A_Grind_163", "A_Grind_164", "A_Grind_165", "A_Grind_166", "A_Grind_167", "A_Grind_170", "A_Grind_171", "A_Grind_172", "A_Grind_173", "A_Grind_174", "A_Grind_175", "A_Grind_176", "A_Grind_177", "A_jamp_A_01", "A_koke_A_L00", "A_koke_A_R00", "A_koke_A1_F00", "A_koke_A2_F00", "A_Koke_B00", "A_Koke_B01", "A_Koke_B02", "A_Koke_F00", "A_Koke_F01", "A_Koke_F02", "A_Koke_G_L01", "A_Koke_G_L02", "A_Koke_G_L03", "A_Koke_G_R01", "A_Koke_G_R02", "A_Koke_G_R03", "A_koke_S_F00", "A_Koke_S_L01", "A_Koke_S_L02", "A_Koke_S_L03", "A_Koke_S_R01", "A_Koke_S_R02", "A_Koke_S_R03", "A_Land_A_Loop", "A_Land_B_A", "A_Land_B_B", "A_Land_B_C", "A_Land_B_D", "A_Land_B_E", "A_Land_B_F", "A_Land_B_G", "A_Land_B_H", "A_Land_B_I", "A_Land_B_J", "A_Land_B_K", "A_Land_B_L", "A_Land_B_Loop", "A_Land_B_M", "A_Land_B_N", "A_Land_B_X", "A_Land_C_Loop", "A_Land_D_Loop", "A_Land_E_Loop", "A_Land_F_A", "A_Land_F_B", "A_Land_F_C", "A_Land_F_D", "A_Land_F_E", "A_Land_F_F", "A_Land_F_G", "A_Land_F_H", "A_Land_F_I", "A_Land_F_J", "A_Land_F_K", "A_Land_F_L", "A_Land_F_Loop", "A_Land_F_M", "A_Land_F_N", "A_Land_F_X", "A_Land_G_Loop", "A_Land_H_Loop", "A_Land_I_Loop", "A_Land_J_Loop", "A_Land_K_Loop", "A_Land_L_A", "A_Land_L_B", "A_Land_L_C", "A_Land_L_D", "A_Land_L_E", "A_Land_L_F", "A_Land_L_G", "A_Land_L_H", "A_Land_L_I", "A_Land_L_J", "A_Land_L_K", "A_Land_L_L", "A_Land_L_Loop", "A_Land_L_M", "A_Land_L_N", "A_Land_L_X", "A_Land_M_Loop", "A_Land_N_Loop", "A_Land_R_A", "A_Land_R_B", "A_Land_R_C", "A_Land_R_D", "A_Land_R_E", "A_Land_R_F", "A_Land_R_G", "A_Land_R_H", "A_Land_R_I", "A_Land_R_J", "A_Land_R_K", "A_Land_R_L", "A_Land_R_M", "A_Land_R_N", "A_Land_R_X", "A_Land_X_Loop", "A_Miss_00", "A_Oti_loop01", "A_pipe_000", "A_pipe_001", "A_Pslide_L01", "A_Pslide_L02", "A_Pslide_L03", "A_Pslide_R01", "A_Pslide_R02", "A_Pslide_R03", "A_push00", "A_push01", "A_Run01", "A_Run01_boko", "A_Run02", "A_Run02_boko", "A_Run03", "A_Run03_boko", "A_Run04", "A_Run04_boko", "A_Run05", "A_Run05_boko", "A_wallride_L01", "A_wallride_R01", "A_Yoro_B", "A_Yoro_dw_B", "A_Yoro_dw_F", "A_Yoro_dw_L", "A_Yoro_dw_R", "A_Yoro_F", "A_Yoro_L", "A_Yoro_R", "Event_093", "Event_094", "Event_102", "Event_165", "Goal_A_Enemy00", "Goal_A_Enemy01", "Goal_B_Enemy00", "Goal_C_Enemy00", "Goal_C_Enemy01", "Goal_D_Enemy00", "Goal_D_Enemy01", "Goal_lose01", "Goal_lose02", "Goal_lose03", "Goal_lose04", "Goal_lose05", "Goal_lose06", "Goal_win01", "Goal_win02", "Goal_win03", "Goal_win04", "Goal_win05", "Goal_win06", "St_01_rdy_dammy01", "Start_01_Boss", "Start_01_CountPlayer", "Start_01_JB", "Start_01_PreCnt", "Start_01_rdy01", "Start_01_rdy01_dammy", "Start_01_rdy02", "Start_01_rdy03", "Start_01_rdy04", "Start_01_rdy05", "Start_01_rdy06", "Start_01_rdy07", "Start_01_rdy08", "Start_01_rdy09", "Start_01_rdy10", "Start_01_Sub", "Start_01_SubBoss", "Start_02_Boss", "Start_02_CountPlayer", "Start_02_PreCnt", "Start_02_rdy01", "Start_02_rdy01_dammy", "Start_02_rdy02", "Start_02_rdy03", "Start_02_rdy04", "Start_02_rdy05", "Start_02_rdy06", "Start_02_rdy07", "Start_02_rdy08", "Start_02_rdy09", "Start_02_rdy10", "Start_02_Sub", "Start_02_SubBoss", "Start_03_Boss", "Start_03_CountPlayer", "Start_03_PreCnt", "Start_03_rdy01", "Start_03_rdy01_dammy", "Start_03_rdy02", "Start_03_rdy03", "Start_03_rdy04", "Start_03_rdy05", "Start_03_rdy06", "Start_03_rdy07", "Start_03_rdy08", "Start_03_rdy09", "Start_03_rdy10", "Start_03_Sub", "Start_03_SubBoss", "Start_04_Boss", "Start_04_CountPlayer", "Start_04_PreCnt", "Start_04_rdy01", "Start_04_rdy01_dammy", "Start_04_rdy02", "Start_04_rdy03", "Start_04_rdy04", "Start_04_rdy05", "Start_04_rdy06", "Start_04_rdy07", "Start_04_rdy08", "Start_04_rdy09", "Start_04_rdy10", "Start_04_Sub", "Start_04_SubBoss", "Start_05_Boss", "Start_05_rdy01", "Start_05_rdy01_dammy", "Start_05_rdy02", "Start_05_rdy03", "Start_05_rdy04", "Start_05_rdy05", "Start_05_rdy06", "Start_05_rdy07", "Start_05_rdy08", "Start_05_rdy09", "Start_05_rdy10", "Start_05_Sub", "Start_05_SubBoss", "Start_06_Boss", "Start_06_rdy01", "Start_06_rdy01_dammy", "Start_06_rdy02", "Start_06_rdy03", "Start_06_rdy04", "Start_06_rdy05", "Start_06_rdy06", "Start_06_rdy07", "Start_06_rdy08", "Start_06_rdy09", "Start_06_rdy10", "Start_06_Sub", "Start_06_SubBoss", "Start_VS", "Start_VS_01", "Start_VS_02", "Start_VS_03", "Start_VS_03_rdy05", "Start_VS_03_rdy06", "Start_VS_03_rdy07", "Start_VS_03_rdy08", "Start_VS_03_rdy09", "Start_VS_04", "Start_VS_04_Boss", "Start_VS_04_Sub", "Start_VS_04_SubBoss", "Start_VS_05", "Start_VS_06", "Start_VS_rdy01", "Start_VS_rdy02", "Start_VS_rdy03", "Start_VS_rdy04"] 

def registerNoesisTypes():
    handle = noesis.register("Ollie King Player models (Arcade)",".mdb")
    noesis.setHandlerTypeCheck(handle, bcCheckType)
    noesis.setHandlerLoadModel(handle, bcLoadModel)
    return 1


# Check file type

def bcCheckType(data):
    return 1


# Create kf joint

def createKfJoint(jointIndex, posKfs, rotKfs):
    kfJoint = NoeKeyFramedBone(jointIndex)
    if (rotKfs):
        kfJoint.setRotation(rotKfs, noesis.NOEKF_ROTATION_QUATERNION_4,noesis.NOEKF_INTERPOLATE_LINEAR)
    if (posKfs):
        kfJoint.setTranslation(posKfs, noesis.NOEKF_TRANSLATION_VECTOR_3,noesis.NOEKF_INTERPOLATE_LINEAR)
    return kfJoint
    
# Read the anim data

def bcLoadAnims(data, animName, joints):
    bs = NoeBitStream(data) #base one
    bs2 = NoeBitStream(data) #used to process timing more easily
    
    bs.seek(0x20)
    kfDataStart = bs.readUInt() + 0x20
    timingDataStart = bs.readUInt() + 0x20
    bs.read('2i') # first = weird framerate ?
    frameCount = bs.readUInt()
    bs.readUInt()
    kfCount = bs.readUInt()
    bs.seek(kfDataStart)
    bs2.seek(timingDataStart)
    
    jointIndex = -1
    prevTiming = 0
    bPosData = False
    kfJoints = []
    rotKfs = []
    posKfs = []
    framerate = 60
    timing = 0
    for i in range(kfCount):
        prevTiming, timing = timing, bs2.readShort()
        if prevTiming > timing:
            if timing == -1: #FFFF, we switch
                if jointIndex >=0:
                    kfJoints.append(createKfJoint(jointIndex, posKfs, rotKfs))
                jointIndex+=1
                posKfs, rotKfs = [], []                                     
                bs.readBytes(0x10)
                timing = 0
                if jointIndex == 1:
                    bPosData = True
            else:
                if jointIndex == 19:               
                    kfJoints.append(createKfJoint(jointIndex, posKfs, rotKfs))
                    jointIndex+=1
                    posKfs, rotKfs = [], []
                    bPosData = True
                    timing = 0
                elif jointIndex == 1 or jointIndex == 20: # Need to add the last pos kf
                    bPosData = False
                    pos = NoeVec3.fromBytes(bs.readBytes(0xC)) # Get the positions AS-IS from the .mtb file
                    ZVAL = pos[0] # First float is actually the Z position value, store here in temp var
                    XVAL = pos[2] # Last float is actually the X position value, store here in temp var
                    pos[0] = XVAL # Swap first float with real X
                    pos[2] = ZVAL # Swap last float with real Z
                    bs.readUInt()
                    posKfs.append(NoeKeyFramedValue(float(timing)/ framerate, pos))
        else:
            if bPosData:
                pos = NoeVec3.fromBytes(bs.readBytes(0xC)) # Same as above method
                ZVAL = pos[0]
                XVAL = pos[2]
                pos[0] = XVAL
                pos[2] = ZVAL
                bs.readUInt()
                posKfs.append(NoeKeyFramedValue(float(timing)/ framerate, pos))
            else:
                quat = NoeQuat.fromBytes(bs.readBytes(0x10))
                quat = NoeQuat([quat[3],quat[2],quat[1],quat[0]]).transpose()
                rotKfs.append(NoeKeyFramedValue(float(timing)/ framerate, quat))
    # Add last joint kfs
    kfJoints.append(createKfJoint(jointIndex, posKfs, rotKfs))
    return NoeKeyFramedAnim(animName, joints, kfJoints, framerate)
            
# Read the model data

def bcLoadModel(data, mdlList):
    bs = NoeBitStream(data)
    ctx = rapi.rpgCreateContext()
    rapi.rpgSetOption(noesis.RPGOPT_TRIWINDBACKWARD,1)

    curr_folder = rapi.getDirForFilePath(rapi.getInputName()).lower()
    curr_file = rapi.getLocalFileName(rapi.getInputName()).lower()

    mesh_name = curr_file.replace(".mdb", "")
    # Some models have motion mesh versions, others are simple versions. If-statement below makes sure that the proper texture file names are read later if selected
    nunoCheck = False
    if "_nuno" in mesh_name:
      mesh_name = mesh_name.replace("_nuno", "")
      nunoCheck = True
    elif "_n" in mesh_name:
        mesh_name = mesh_name.replace("_n", "") 
    elif "_s" in mesh_name:
        mesh_name = mesh_name.replace("_s", "")

    txb_file = curr_folder + mesh_name + ".txb"
    mesh_num = 0

    if rapi.checkFileExists(txb_file):
        tex_file = NoeBitStream(rapi.loadIntoByteArray(txb_file))
        mat_list, tex_list = ReadTextures(tex_file)
    else:
        print("Unable to load texture file")
        mat_list = []
        tex_list = []

    bones = []
    bone_num = 0

    parent_info = [-1, 0, 1, 2, 3, 4, 4, 6, 7, 8, 4, 10, 11, 12, 1, 14, 15, 1, 17, 18, 0]				# default parent info for all player model skeletons
    # The if-statement branch below gives the proper parenting to the motion meshes when loaded in. The two characters with exceptions to the norm have their own included here.
    if nunoCheck == True:
        if "didi" in mesh_name:
            parent_info = [-1, 0, 1, 0, 3, 0, 5, 0, 7, 0, 9]				# parent info for didi motion mesh skeleton
        elif "grinner" in mesh_name:
            parent_info = [-1, 0, 1, 2, 3, 4, 0, 6, 7, 8, 9, 0, 11, 12, 13, 14, 0, 16, 17, 18, 19]				# parent info for grinner motion mesh skeleton
        else:
            parent_info = [-1, 0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19]              # default parent info for other motion mesh skeletons

    bs.seek(8)
    table2 = bs.readUInt() + 0x20
    table2_size = bs.readUInt()
    table1 = bs.readUInt()
    entries = bs.readUInt()

    print("table2 - 0x20: " + hex(table2 - 0x20)) # Table sometimes gets populated, print some info on it.
    print("table2: " + hex(table2)) # Table sometimes gets populated, print some info on it.
    print("Entries: " + str(entries)) # No entries happen, which mean loop never starts.

    for a in range(entries):
        bs.seek(table2 + (a * 0x20))
        print("bone table offset: " + hex(bs.seek(table2 + (a * 0x20))))
        offset = bs.readUInt() + 0x20
        print("bone identifier offset - 0x20: " + hex(offset - 0x20))
        print("bone identifier offset: " + hex(offset))
        offset2 = bs.readUInt() + 0x20
        print("offset2 - 0x20: " + hex(offset2 - 0x20))
        print("offset2: " + hex(offset2))
        tex_num = bs.readUInt()
        print("text_num: " + hex(tex_num))
        bs.seek(offset)
        prim_type = bs.readUInt()							# 4 = triangles, 5 = strips
        entry_type = bs.readUInt()

        if entry_type == 0x112:							# bone info
            bs.seek(offset + 0x20)
            print("bone position offset: " + hex(bs.seek(offset + 0x20)))
            pos = NoeVec3.fromBytes(bs.readBytes(12))
            matrix = NoeAngles([0,0,90]).toMat43()
            pos[2] *= -1 # had to add this recently, something changed with the script and it didn't automatically fix it anymore so this properly flips Z coords of bone position to be on the mesh
            matrix[3] = pos
            bones.append(NoeBone(bone_num, "Bone_" + str(bone_num), matrix, None, parent_info[bone_num]))
            bone_num += 1

        elif entry_type == 0x1118:							# mesh info, stride 0x28
            vert_offset = bs.readUInt() + 0x20
            print("vert_offset: " + hex(vert_offset))
            vert_count = bs.readUInt()
            print("vert_count: " + str(vert_count))
            face_offset = bs.readUInt() + 0x20
            print("face_offset: " + hex(face_offset))
            face_count = bs.readUInt()
            print("face_count: " + str(face_count))

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
    
    # animations
    anims = []
    dataTemp = None
    selectAllAnims = noesis.userPrompt(noesis.NOEUSERVAL_INT, "Load all animations?", "Type 1 to load all anims in the motion folder, 0 to select animations, or cancel to load none.", "0")
    if selectAllAnims == 1:
        for i in range (613):
            mtb_file = curr_folder + "\Motion\\" + animNames[i] + ".mtb" # Get the file path and increment through them sequentially.
            if rapi.checkFileExists(mtb_file):
                dataTemp = rapi.loadIntoByteArray(mtb_file) # Loads it into the byte array, file is sent to append to the model in the last line of this loop
            else:
                print("Animations not found.") # Error message if the director is not located
            anims.append(bcLoadAnims(dataTemp, animNames[i], bones)) # After import, append to rig
    elif selectAllAnims == 0:
        animPath = rapi.loadPairedFileGetPath("animation file", ".mtb")
        while(animPath):
            animName = os.path.basename(animPath[1])[:-4] # Filename without extension
            anims.append(bcLoadAnims(animPath[0], animName, bones)) # After import, append to rig

            animPath = rapi.loadPairedFileGetPath("animation file", ".mtb")
    else: 
        None

    try:
        mdl = rapi.rpgConstructModel()
    except:
        mdl = NoeModel()

    mdl.setModelMaterials(NoeModelMaterials(tex_list, mat_list))
    mdl.setBones(bones)
    if anims:
        mdl.setAnims(anims)
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
