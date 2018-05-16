class Board:

    def __init__(self):

        self.visual_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.last_pos = None
        self.last_token = None

    # Basic board structure
    # Added extra padding on both sides for better readibility
    def draw_board(self):
        print("""
           {}  |  {}  |  {}
         -----------------
           {}  |  {}  |  {}
         -----------------
           {}  |  {}  |  {}
        """.format(*self.visual_board))

    # Insert will update the actual board data
    # then update the visual board to be displayed
    def insert_board(self, position, player):
        self.board[position] = player
        self.update_visual(position, player)

    # Used to highlight the last move made
    def update_visual(self, position, player):

        # Check if previous move exists, if not, current move
        # becomes the last move. Otherwise, change the visual back
        # to normal for the last move and highlight the current move
        if self.last_pos is not None:
            self.visual_board[self.last_pos] = self.last_token

        self.last_pos = position
        self.last_token = player

        # Underline the last played spot on the board
        self.visual_board[position] = "\033[4m{}\033[0m".format(player)

    def available_moves(self):
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
