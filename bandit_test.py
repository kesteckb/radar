import random
    
def sweep(position) -> tuple:
    x_shift = random.randrange(-1, 1)
    y_shift = random.randrange(-1, 1)
    
    if position == None:
        start_position = (420, 260)
    else:
        start_position = position
    
    new_position = (start_position[0] + x_shift, start_position[1] + y_shift)
    start_position = new_position
    
    return new_position