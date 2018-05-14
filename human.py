from player import *

class Human(Player):

    def __init__(self, name):
        super().__init__(name)

    def make_a_move(self):
        print("Making a move!")
