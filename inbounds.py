from math import sqrt

def is_inbounds(x, y):
    distance = sqrt(pow((400 - x), 2) + pow((415 - y), 2))
    
    if y > 415:
        return False
    elif distance > 350:
        return False
    elif distance > 265 and y > 280:
        return False
    elif (x < 130 or x > 675) and y > 255:
        return False
    else:
        return True