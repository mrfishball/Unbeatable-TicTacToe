import unittest
from io import StringIO
from unittest import mock
from game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_game_mode(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=["1", "2", "3"]):
            self.assertEqual(self.game.set_game_mode(), 1)
            self.assertEqual(self.game.set_game_mode(), 2)
            self.assertEqual(self.game.set_game_mode(), 3)

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_players(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=["Lee", "John", "Mary"]):
            self.game.set_players(1)
            self.assertEqual(self.game.player1.name, "Lee")
            self.assertEqual(self.game.player2.name, "Iris (AI)")

            self.game.set_players(2)
            self.assertEqual(self.game.player1.name, "John")
            self.assertEqual(self.game.player2.name, "Mary")

            self.game.set_players(3)
            self.assertEqual(self.game.player1.name, "Iris (AI)")
            self.assertEqual(self.game.player2.name, "Betty (AI)")

    # @mock.patch("sys.stdout", new_callable=StringIO)
    # def test_set_token(self, mock_stdout):
    #     with mock.patch("builtins.input", side_effect=[]):
    #         self.game.set_token


if __name__ == '__main__':
    unittest.main()
