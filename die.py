from random import randint

class Die:
    # a class representing a single die

    def __init__(self, num_sides=6):
        # assume a six sided die
        self.num_sides = 6

    def roll(self):
        # return rand value between 1 and num of sides
        return randint(1, self.num_sides)