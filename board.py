class Board:

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.last_pos = None
        self.last_token = None

    # Basic board structure
    # Added padding on both sides for better readibility
    # def draw_board(self, board):
    def draw_board(self):
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def insert(self, position, player):

        if self.last_pos is not None:
            self.board[self.last_pos] = self.last_token

        self.last_pos = position
        self.last_token = player
        self.board[position] = "({})".format(player)

    def available_moves(self, tokens):
        return [pos for pos, spot in enumerate(self.board) if isinstance(spot, int)]

    def isValidMove(self, move):
        try:
            move = int(move)
            if move in self.board:
                return True
            else:
                print("\nThe move is either taken or invalid. Please try again.")
                return False
        except (TypeError, ValueError, IndexError) as e:
            print("\nThat is not a valid move. Please try again.")
            return False
