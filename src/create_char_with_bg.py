# Built with python 3, dependencies installed with pip 

# This module provides access to the mathematical functions defined by the C standard.
# https://docs.python.org/3/library/math.html
import math

# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

font = ImageFont.truetype("fonts/OpenSans-Light.ttf", 8)
bgImg = Image.open("background/heic2018b.jpg").convert("RGBA")

(bgW, bgH) = bgImg.size

blockW = 600
blockH = 500

charW = 240
charH = 240

maxX = math.floor(bgW / blockW)
maxY = math.floor(bgH / blockH)

# background image might not be an exact multiple of block size
# so we calculate the offset to extract blocks from the middle
# of the background
osX = (bgW - (maxX * blockW)) / 2
osY = (bgH - (maxY * blockH)) / 2

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = (480, 480)

# calculate offset of character within background block
charOSx = math.floor((blockW - dimensions[0]) / 2)
charOSy = math.floor((blockH - dimensions[1]) / 2)

def main():
    for x in range(0, maxX - 1):
        for y in range(0, maxY - 1):
            coord = str(x) + "," + str(y)
            print(coord)

            cropX = x * blockW
            cropY = y * blockH
            
            block = bgImg.crop((cropX, cropY, cropX + blockW - 1, cropY + blockH - 1))
            
            # create canvas called draw
            draw = ImageDraw.Draw(block)
            draw.text((5,5), coord, (255, 255, 255), font=font)

            block.alpha_composite(genChar(), (charOSx, charOSy))

            block.save("blocks/block_" + str(x) + "_" + str(y) + ".png")



def genChar():
    # using ETH block number as starting random number seed
    c=randint(0,500)
    seed(c)

    #body color - randomly generate each number in an RGB color
    bd = (randint(0, 256), randint(0, 256), randint(0, 256), 255)
    c=randint(0,500)
    seed(c)

    #throat color - same as head color
    fa = (randint(0, 256), randint(0, 256), randint(0, 256), 255)
    d = randint(0,1000)
    seed(d)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255, 255)
        ey = (0, 0, 0, 255)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256), 255)
        ey = (154, 0, 0, 255)
    e = randint(0,1000)
    seed(e)

    # beak color
    f = randint(0, 1000)
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

    # background color
    bg = (255, 255, 255, 0)

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
    
    crab_invader = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bd, bd, fa, fa, ew, ew, fa, fa, fa, fa, fa, fa, ew, ew, fa, fa, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, fa, fa, ey, ew, fa, fa, fa, fa, fa, fa, ey, ew, fa, fa, bd, bd, bg, bg, bg],
        [bg, bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd, bg],
        [bg, bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd, bg],
        [bg, bk, bk, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bk, bk, bg],
        [bg, bk, bk, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bk, bk, bg],
        [bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bk, bk, bg, bg, bk, bk, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bk, bk, bg, bg, bk, bk, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    crab_invader_sunglasses = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, ey, ey, ey, ey, ew, ew, ey, ey, ey, ey, ey, ey, ew, ew, ey, ey, ey, ey, bg, bg, bg],
        [bg, bg, bg, ey, ey, ey, ey, ew, ew, ey, ey, fa, fa, ey, ey, ew, ew, ey, ey, ey, ey, bg, bg, bg],
        [bg, bg, bg, ey, ey, ey, ey, ey, ey, ey, ey, fa, fa, ey, ey, ey, ey, ey, ey, ey, ey, bg, bg, bg],
        [bg, bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd, bg],
        [bg, bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd, bg],
        [bg, bk, bk, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bk, bk, bg],
        [bg, bk, bk, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bk, bk, bg],
        [bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bk, bk, bg, bg, bk, bk, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bk, bk, bg, bg, bk, bk, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    ufo = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bg, bg, bg],
        [bg, ol, ol, bd, fa, bk, bk, fa, fa, fa, fa, bk, bk, fa, fa, fa, fa, bk, bk, fa, bd, ol, ol, bg],
        [bg, ol, ol, bd, fa, bk, bk, fa, fa, fa, fa, bk, bk, fa, fa, fa, fa, bk, bk, fa, bd, ol, ol, bg],
        [bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd],
        [bd, bd, bd, bd, bd, bd, bd, bd, bd, ol, ol, bd, bd, ol, ol, bd, bd, bd, bd, bd, bd, bd, bd, bd],
        [bg, bg, bg, ol, ol, bd, bd, ol, ol, bg, bg, bd, bd, bg, bg, ol, ol, bd, bd, ol, ol, bg, bg, bg],
        [bg, bg, bg, ol, ol, bd, bd, ol, ol, bg, bg, bk, bk, bg, bg, ol, ol, bd, bd, ol, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bk, bk, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bk, bk, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    eagle = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bd, bd, fa, fa, ew, ew, fa, fa, fa, fa, fa, fa, ew, ew, fa, fa, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, fa, fa, ey, ew, fa, fa, fa, fa, fa, fa, ey, ew, fa, fa, bd, bd, bg, bg, bg],
        [bg, bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd, bg],
        [bg, bd, bd, bd, bd, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, fa, bd, bd, bd, bd, bg],
        [bg, bk, bk, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bk, bk, bg],
        [bg, bk, bk, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bk, bk, bg],
        [bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bk, bk, bg, bg, bk, bk, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bk, bk, bg, bg, bk, bk, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    cockatoo = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd, bd, bd, bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd, bd, bd, bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, ol, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, ew, ew, ey, ey, bd, bd, ew, ew, ey, ey, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, ew, ew, ey, ey, bd, bd, ew, ew, ey, ey, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, ew, ew, ew, ew, bd, bd, ew, ew, ew, ew, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, ew, ew, ew, ew, bd, bd, ew, ew, ew, ew, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg],
        [bg, bg, bg, bd, bd, bd, bd, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bd, bd, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bd, bd, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bd, bd, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, bd, bd, bg, bg, bg, bg, bd, bd, bg, bg, bd, bd, bg, bg, bg, bg, bd, bd, bg, bg, bg],
        [bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg],
        [bg, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, ol, ol, bg, bg, bg, bg, ol, ol, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    # choose which space invader image to use
    seed(f)
    g = randint(0,1000)
    if g > 250:
        # if random number is 251 - 1000 >> crab invader
        pixels = crab_invader
    elif 250 >= g > 100:
        # 101 - 250 >> crab invader sunglasses
        pixels = crab_invader_sunglasses
    elif 100 >= g > 40:
        # 41 - 100 >> ufo
        pixels = ufo
    elif 40 >= g > 5:
        # 6 - 40 >> eagle
        pixels = eagle
    else:
        # if random number is 5 or less >> cockatoo!!
        pixels = cockatoo

    # convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array, "RGBA")
    new_image = new_image.resize(dimensions, resample=0)
    
    return new_image

# this allows us to specify our functions in any order
# iso having to define them before they are called
if __name__=="__main__":
   main()

