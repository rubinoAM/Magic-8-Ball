from random import randrange

class Eightball(object):
    def __init__(self):
        self.name = "Eightball"
        self.initial_state = 0
    def roll(self):
        roll = randrange(0,21)
        return roll