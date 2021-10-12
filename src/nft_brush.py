# 2021-10-11
# NFT Brush v1.0
# 
# Usage: nft_brush.py <background-image-path> <output-path>
#
# Splits background image into blocks of width and height blockW and blockH respectively.
# Draws generated sprites with random colours, onto the blocks according to the defined
# probability distribution for each sprite.
# Saves blocks and complete image in output-path.
#

# Built with python 4, dependencies installed with pip 

import os
import math
import numpy
import random

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Import sprite generator modules
from sprites import octopus
from sprites import crab
from sprites import squid
from sprites import cuttlefish
from sprites import ufo

# Store references of above sprite generation modules in an dictionary with probablility percentages for each
# sprite.
# Probablilities be specified from most to least common because in genSpriteOccurrenceList, we add a first
# type in case of rounding errors
spriteFunctionProbabilityTable = {
    "octopus"   : (35, octopus   ), 
    "crab"      : (30, crab      ), 
    "squid"     : (12, squid     ), 
    "cuttlefish": (13, cuttlefish), 
    "ufo"       : (10, ufo       )
}

# initialise random number generator with current system time
random.seed()

imageName = "heic2018b.jpg"

font = ImageFont.truetype("fonts/OpenSans-Light.ttf", 8)
bgImg = Image.open("background/" + imageName).convert("RGBA")

(bgW, bgH) = bgImg.size

blockW = 600
blockH = 500

# final sprite dimensions
# the original 24x24 pixel image will be expanded to these dimensions
spriteW = 480
spriteH = 480

maxX = math.floor(bgW / blockW)
maxY = math.floor(bgH / blockH)

# background image might not be an exact multiple of block size
# so we calculate the offset to extract blocks from the middle
# of the background
osX = round((bgW - (maxX * blockW)) / 2)
osY = round((bgH - (maxY * blockH)) / 2)

# calculate offset of sprite within background block
spriteOSx = math.floor((blockW - spriteW) / 2)
spriteOSy = math.floor((blockH - spriteH) / 2)

# dimensions of full image
imageW = 1024
imageH = 768

#==============================================================================
def main():
    print("Generating", maxX * maxY, "blocks...")

    spriteOccurrenceList = shuffle(genSpriteOccurrenceList(spriteFunctionProbabilityTable, maxX * maxY))

    spriteNo = 0

    # paste generated sprites onto full image
    print("generating sprites...")

    for x in range(0, maxX):
        for y in range(0, maxY):
            coord = str(x) + "," + str(y)
            print(x, ",", y)

            blockX = x * blockW
            blockY = y * blockH

            # generate 24 x 24 sprite
            sprite = genSprite(spriteOccurrenceList[spriteNo])

            fullSizeSprite = sprite.resize((spriteW, spriteH), resample=0)

            bgImg.alpha_composite(fullSizeSprite, (osX + blockX + spriteOSx, osY + blockY + spriteOSy))

            spriteNo += 1

    fullImageShrunk = bgImg.resize((imageW, imageH), resample=0)
    fullImageShrunk.convert("RGB").save("blocks/full.jpg")

    # split full image into blocks
    print("splitting blocks...")
    for x in range(0, maxX):
        for y in range(0, maxY):
            coord = str(x) + "," + str(y)
            print(coord)

            cropX = osX + (x * blockW)
            cropY = osY + (y * blockH)
            
            block = bgImg.crop((cropX, cropY, cropX + blockW - 1, cropY + blockH - 1))
            
            # create canvas called draw
            draw = ImageDraw.Draw(block)
            draw.text((5,5), coord, (255, 255, 255), font=font)

            block.save("blocks/block_" + str(x) + "_" + str(y) + ".png")


#==============================================================================
# given a list of [sprite_name, probability] and a number of blocks
# returns a randomly ordered list of length blocks-long, with the
# sprite names occurring as many times as specified by their respective
# probabilities
#==============================================================================
def genSpriteOccurrenceList(probTable, numBlocks):
    print("\nGenerating sprite occurrence list...")
    result = []

    # for each sprite
    for spriteName in probTable.keys():
        (prob, module) = probTable[spriteName]

        # how many times do we have to generate this particular sprite ("prob % of numBlocks")
        spritesToGenerate = round(numBlocks * prob / 100)

        print((spriteName + "               ")[0: 15], ": x", spritesToGenerate, "(", prob, "%)")

        # accessories have their own probability of being present
        accessoryMap = module.accessoryMap()

        # accessoryMap format:
        #    #         name           probability%   value
        #    return { "sunglasses": ( 50           , [...])
        #           }
        #

        # generate sprites with accessories
        generatedSprites = 0
        for (accessoryProb, accessory) in accessoryMap.values():
            accessoriesToGenerate = round(accessoryProb * spritesToGenerate / 100)
            for x in range(accessoriesToGenerate):
                result.append((spriteName, accessory))
                generatedSprites += 1


        # generate the rest of spritesToGenerate that have no accessory
        for x in range(generatedSprites, spritesToGenerate):
            result.append((spriteName, None))



    # due to rounding errors, result list might be 1 element shorter than numblocks
    for x in range(len(result), numBlocks):
        result.append(result[0])


    return result


def shuffle(list):
    print("\nShuffling list...")
    maxIdx = len(list) - 1
    
    for x in range(len(list)):
        rand = random.randint(0, maxIdx)
        #swap values
        list[x], list[rand] = list[rand], list[x]
        print("swapped: ", x, "with", rand)

    return list

#==============================================================================
def genSprite(spriteEntry):
    # background color
    bg = (255, 255, 255, 0)

    #body color - randomly generate each number in an RGB color
    bd = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256), 255)

    #throat color - same as head color
    fa = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256), 255)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    d = random.randint(0,1000)
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255, 255)
        ey = (0, 0, 0, 255)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256), 255)
        ey = (154, 0, 0, 255)

    # beak color
    f = random.randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> grey beak
        bk = (152, 152, 152, 255)
    elif 500 >= f > 47:
        # 48-500 >> gold beak
        bk = (204, 172, 0, 255)
    elif 47 >= f > 7:
        # 8 >> 47 >> red beak
        bk = (204, 0, 0, 255)
    else:
        # random number is 7 or less >> black beak
        bk = (0, 0, 0, 255)

    # outline color
    # ol = (0, 0, 0)
    salt = 15
    
    ol_list = []
    
    for c in bd:
        if c + salt > 100:
            ol_list.append(255)
        else:
            ol_list.append(c + salt)
    
    ol = tuple(ol_list)

    (spriteName, accessory) = spriteEntry
    
    # get the (probablility, modulename) value from ditionary for current spriteName
    (_, spriteModule) = spriteFunctionProbabilityTable[spriteName]

    # call the generate function on the selected module
    pixels = spriteModule.genSprite(bg, bd, fa, ew, ey, bk, ol)

    if accessory is not None:
        for x in range(len(pixels)):
            for y in range(len(pixels[x])):
                if accessory[x][y] is not None:
                    pixels[x][y] = accessory[x][y]

    # convert the pixels into an array using numpy
    array = numpy.array(pixels, dtype=numpy.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array, "RGBA")
    
    return new_image

#==============================================================================
# this allows us to specify our functions in any order
# iso having to define them before they are called
if __name__=="__main__":
   main()
