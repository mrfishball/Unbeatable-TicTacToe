import unittest
from human import *
from board import *

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.player = Human("Peter")
        self.player.token = "X"
        self.board = Board()

        self.player2 = Human("Leo")
        self.player2.token = "O"

    # Test when function is called, the board and visual board are both updated to reflect change
    # Calling insert will also trigger update visual
    def test_insert_board_and_update_visual(self):

        self.board.insert_board(4, self.player.token)
        self.assertEqual(self.board.board[4], self.player.token)
        self.assertEqual(self.board.visual_board[4], "\033[4m{}\033[0m".format(self.player.token))
        self.assertEqual(self.board.last_pos, 4)
        self.assertEqual(self.board.last_token, self.player.token)

        # Test insert doesn't undo any move currently exists
        # Test that insert calls update visual to update last pos and last token played correctly
        self.board.insert_board(1, self.player2.token)
        self.assertEqual(self.board.board[4], self.player.token)
        self.assertEqual(self.board.board[1], self.player2.token)
        self.assertEqual(self.board.visual_board[4], self.player.token)
        self.assertEqual(self.board.visual_board[1], "\033[4m{}\033[0m".format(self.player2.token))
        self.assertEqual(self.board.last_pos, 1)
        self.assertEqual(self.board.last_token, self.player2.token)

if __name__ == '__main__':
    unittest.main()
