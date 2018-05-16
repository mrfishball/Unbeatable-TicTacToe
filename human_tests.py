import unittest
from unittest import mock
from io import StringIO
from human import *
from board import *

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.player = Human("Ben")
        self.board = Board()
        self.player.token = "X"

        self.player2 = Human("Ben")
        self.player2.token = "O"

    # Test that the function handle user input correctly
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_make_a_move(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", "0", "a", "5", "5", "8"]):

            # All invalid inputs should be ignored and the fucntion should only return
            # when a valid input is entered, then register move onto the board
            result = self.player.make_a_move(self.board)
            self.assertEqual(result, 5)
            self.assertEqual(self.board.board[result-1], self.player.token)

            # When a spot that has already been taken is enter, it should be treated as invalid move
            # The spot taken should have the original token still in place
            result2 = self.player2.make_a_move(self.board)
            self.assertEqual(result2, 8)
            self.assertEqual(self.board.board[result2-1], self.player2.token)
            self.assertEqual(self.board.board[result-1], self.player.token)

if __name__ == '__main__':
    unittest.main()
