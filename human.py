from player import *
import util

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.dice = None

    def make_a_move(self, board):
        move = util.get_human_spot(board, self)
        board.insert_board(move, self.token)
        return move + 1
