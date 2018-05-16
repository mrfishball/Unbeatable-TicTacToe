import unittest
from io import StringIO
from unittest import mock
from game import *

class TestUtil(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    # Test that the function handles user input for a move correctly
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_get_human_spot(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", "12", "a", "0", "3", "8"]):
            player = Human("Tony")
            player.token = "X"
            result = util.get_human_spot(self.game.board, player)
            self.assertEqual(result, 2)

            result = util.get_human_spot(self.game.board, player)
            self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
