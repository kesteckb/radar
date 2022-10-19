from math import sqrt
HDG_LINE_LENGTH = 18

class Bandit():
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.prev_x = None
        self.prev_y = None

    def __str__(self):
        return f"x: {self.pos_x}\ty: {self.pos_y}"

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_position(self):
        return (self.pos_x, self.pos_y)

    def set_previous(self, position):
        pos_x, pos_y = position
        self.prev_x = pos_x
        self.prev_y = pos_y

    def get_previous(self):
        return (self.prev_x, self.prev_y)

    def get_direction(self):
        pointer_x = (self.pos_x - self.prev_x)
        pointer_y = (self.pos_y - self.prev_y)
        slope = pointer_y / pointer_x
        
        if self.pos_x < self.prev_x:
            x_change = -sqrt(pow(HDG_LINE_LENGTH, 2) / (pow(slope, 2) + 1))
            if slope > 0:
                y_change = -sqrt(pow(HDG_LINE_LENGTH, 2) / (1 + (1 / pow(slope, 2))))
            else:
                y_change = sqrt(pow(HDG_LINE_LENGTH, 2) / (1 + (1 / pow(slope, 2))))

        else:
            x_change = sqrt(pow(HDG_LINE_LENGTH, 2) / (pow(slope, 2) + 1))
            if slope > 0:
                y_change = -sqrt(pow(HDG_LINE_LENGTH, 2) / (1 + (1 / pow(slope, 2))))
            else:
                y_change = sqrt(pow(HDG_LINE_LENGTH, 2) / (1 + (1 / pow(slope, 2))))

        return (round(x_change + self.pos_x), round(y_change + self.pos_y))

# Test
# b1 = Bandit(300, 200)
# b1.set_prev(b1.get_pos())
# b1.set_pos(270, 280)
# b1.get_direction()