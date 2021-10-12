def genSprite(bg, bd, fa, ew, ey, bk, ol):
    return [
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

def combine(a, b):
    cols = []
    for x in range(len(a)):
        rows = []
        cols.append(rows)

        for y in range(len(a[x])):
            if a[x][y] is not None:
                rows.append(a[x][y])
            else:
                rows.append(b[x][y])

    return cols

# create a map of accessories
def accessoryMap():
    #         name           probability%   variable name
    return { "sunglasses": ( 10           , sunglasses) 
           , "crown"     : ( 10           , crown     )
           , "sun_crown" : ( 10           , combine(sunglasses, crown)) 
           }               #  ^- this must be less than 100, If it totals 100 then all sprites will have accessories

# define fixed colours here

#       R    G    B    A
bg = None # do nothing
er = (  0,   0,   0,   0)   # overwrite original with transparency
sg = (  0,   0,   0, 255)   # black
cr = (191, 145,  59, 255)   # gold crown colors
ol = (223, 200, 157, 255)   # very soft orange
ru = (155,  17,  30, 255)   # ruby red

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
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, sg, bg, bg, bg],
    [bg, bg, bg, bg, sg, sg, sg, sg, sg, sg, sg, bg, bg, sg, sg, sg, sg, sg, sg, sg, bg, bg, bg, bg],
    [bg, bg, bg, bg, sg, sg, sg, sg, sg, sg, sg, bg, bg, sg, sg, sg, sg, sg, sg, sg, bg, bg, bg, bg],
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

crown = [
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, cr, cr, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, er, er, er, er, bg, bg, bg, cr, cr, bg, bg, bg, er, er, er, er, bg, bg, bg, bg],
    [bg, bg, bg, bg, cr, cr, er, er, bg, cr, cr, cr, cr, cr, cr, bg, er, er, cr, cr, bg, bg, bg, bg],
    [bg, bg, bg, bg, cr, cr, er, er, er, cr, cr, cr, cr, cr, cr, er, er, er, cr, cr, bg, bg, bg, bg],
    [bg, bg, bg, bg, cr, cr, ol, ol, cr, cr, cr, ru, ru, cr, cr, cr, ol, ol, cr, cr, bg, bg, bg, bg],
    [bg, bg, bg, bg, cr, cr, ol, ol, cr, cr, cr, ru, ru, cr, cr, cr, ol, ol, cr, cr, bg, bg, bg, bg],
    [bg, bg, bg, bg, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, bg, bg, bg, bg],
    [bg, bg, bg, bg, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, cr, bg, bg, bg, bg],
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
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
    [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
]
