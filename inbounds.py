# This function is NOT dynamic for different screen resolutions!

from math import sqrt

def is_inbounds(x: int, y: int) -> bool:
    radius = sqrt(pow((400 - x), 2) + pow((415 - y), 2))
    
    if y > 415:
        return False
    elif radius > 350:
        return False
    elif radius > 265 and y > 280:
        return False
    elif (x < 130 or x > 675) and y > 255:
        return False
    else:
        return True


# Tests
assert(is_inbounds(400, 416)) == False
assert(is_inbounds(400, 415)) == True
assert(is_inbounds(400, 50)) == False
assert(is_inbounds(115, 235)) == True
assert(is_inbounds(125, 300)) == False
assert(is_inbounds(680, 315)) == False
assert(is_inbounds(500, 150)) == True
assert(is_inbounds(450, 400)) == True
assert(is_inbounds(630, 450)) == False
assert(is_inbounds(635, 135)) == False