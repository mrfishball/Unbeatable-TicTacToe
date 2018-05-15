from player import *

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.dice = None

    def set_dice(self, diceroll):
        self.dice = diceroll

    def make_a_move(self, game):
        move = self.get_human_spot(game.board)
        game.board.update_visual(move, self.token)
        return move + 1

    def get_human_spot(self, board):
      spot = input("{}, please make a move on the board (1 - 9): ".format(self.name))
      while not board.isValidMove(spot):
        spot = input("{}, please make a move on the board (1 - 9): ".format(self.name))
      spot = int(spot)
      return spot-1
