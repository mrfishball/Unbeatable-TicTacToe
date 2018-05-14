class Board:

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def draw_board(self):
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def register_move(self, position, player):
        self.board[position] = player

    def available_moves(self, token1, token2):
        return [pos for pos, spot in enumerate(self.board) if spot != token1 and spot != token2]

    def isValidMove(self, move):
        try:
            move = int(move)
            if move in board:
                return True
            else:
                print("\nThe move is either taken or invalid. Please try again.")
                return False
        except (TypeError, ValueError, IndexError) as e:
            print("\nThat is not a valid move. Please try again.")
            return False
