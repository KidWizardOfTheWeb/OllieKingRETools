# Ollie King (Arcade)
# Original Noesis script by Dave, 2021
# Derived texture section to separate script by KC
# Last updated: 9 August 2022

# ** WORK IN PROGRESS! **


from inc_noesis import *


def registerNoesisTypes():
    handle = noesis.register("Ollie King Textures (Arcade)",".txb")
    noesis.setHandlerTypeCheck(handle, bcCheckType)
    noesis.setHandlerLoadRGBA(handle, bcLoadRGBA)
    return 1


# Check file type

def bcCheckType(data):
    return 1


# Read the Texture data

def bcLoadRGBA(data, tex_list):
    ctx = rapi.rpgCreateContext()
    bs = NoeBitStream(data)

    bs.seek(4)
    tex_count = bs.readUInt()
    print("Tex count: ", tex_count)

    offset = 0x20
    file_name = rapi.getLocalFileName(rapi.getInputName()).lower()

    for a in range(tex_count):
        tex1 = None # Added because certain textures throw an error based on assigning too early.
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

        elif img_type == 4:					
            raw_image = rapi.imageDecodeRaw(raw_image, width, width, "b4g4r4a4")
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_RGBA32)

        elif img_type == 9: # Similar to 8, listed as different image type
            tex1 = NoeTexture("Texture_" + str(a) + ".bmp", width, width, raw_image, noesis.NOESISTEX_DXT5)

        elif img_type == 6: # Used for first image of s3_tenkyu and obi. They are different formats however, so edgecase is used.
            if file_name == "obi.txb":
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

        offset += data_size + 0x20

    if not tex_list:
        print("No textures found.")
    return 1
