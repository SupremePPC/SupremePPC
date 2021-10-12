def genSprite(bg, bd, fa, ew, ey, bk, ol):
    return [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, ew, ew, ew, bd, bd, bd, bd, ew, ew, ew, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, ew, ew, ey, bd, bd, bd, bd, ew, ew, ey, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg],
        [bg, bg, bg, bg, ol, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, ew, ew, ew, ew, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bd, bd, bd, ew, ew, ew, ew, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bd, bd, bd, bd, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, ol, ol, ol, ol, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bd, bd, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, fa, fa, bg, bg, bg, bg, fa, fa, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

# create a map of accessories
def accessoryMap():
    #         name            probability%   variable name
    return {"stonner_eyes"    :  ( 20      , stonner_eyes)
           ,"sunglasses"      :  ( 20      , sunglasses    )
           ,"three_d_glasses" :  ( 20      ,three_d_glasses)
           }

# define fixed colours here

#       R    G    B    A
bg = None # transparent
wf = (  255,   255,   255, 255)   # white
rl = (  255,     0,     0, 255)   # red
bl = (  0,     255,   255, 255)   # blue
fr = (  0,   0,   0, 255)   # black
ey = (  0,   0,   0, 255)   # black


# define each accessory here using only fixed colours defined above.
# this variable name goes in accessoryMap
sunglasses = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, fr, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, fr, fr, fr, fr, fr, bg, bg, fr, fr, fr, fr, fr, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

three_d_glasses = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, wf, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, wf, rl, rl, rl, wf, wf, wf, wf, bl, bl, bl, wf, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, wf, wf, wf, wf, wf, bg, bg, wf, wf, wf, wf, wf, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

stonner_eyes = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, wf, ey, wf, bg, bg, bg, bg, wf, ey, wf, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, wf, wf, wf, bg, bg, bg, bg, wf, wf, wf, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]

