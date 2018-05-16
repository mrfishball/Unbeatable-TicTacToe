import unittest
from io import StringIO
from unittest import mock
from game import *

class TestUtil(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.players = []
        self.tokens = []

        self.player = Human("Tony")
        self.player.token = "X"

        self.player2 = Human("Lisa")
        self.player.token = "O"

        self.game_order = []

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_get_name_input(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", " Lee", " John ",]):

            # Test that user input is stripped of whitespace before returning
            # Once input is accepted, it should be added to the players array
            result = util.get_name_input(self.players)
            self.assertEqual(result, "Lee")

            result = util.get_name_input(self.players)
            self.assertEqual(result, "John")
            self.assertTrue(len(self.players) == 2)

    # Test that the function handles user input for a move correctly
    # Invalid inputs should be disregarded
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_get_human_spot(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", "12", "a", "0", "3", "8"]):

            result = util.get_human_spot(self.board, self.player)
            self.assertEqual(result, 2)

            result = util.get_human_spot(self.board, self.player)
            self.assertEqual(result, 7)

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_get_token_input(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", "1", "$", "d", "D", "d", "F"]):

            # Test that invalid inputs are ignored
            # only valid inputs will be returned
            result = util.get_token_input(self.player.name, self.tokens)
            self.assertEqual(result, self.tokens[0].upper())
            self.assertEqual(result, "D")

            # Test for token token duplication handling
            result = util.get_token_input(self.player2.name, self.tokens)
            self.assertEqual(result, self.tokens[1].upper())
            self.assertEqual(result, "F")

    def test_generate_token(self):
        self.tokens = []
        result = util.generate_token(self.tokens)
        self.assertTrue(self.tokens[0], result)

        result2 = util.generate_token(self.tokens)
        self.assertTrue(self.tokens[1], result2)
        self.assertNotEqual(result, result2)

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_turn_helper(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", "a", "3", "1", "2"]):
            util.set_turn_helper(self.game_order, self.player, self.player2)
            self.assertEqual(self.game_order[0], self.player)
            self.assertEqual(self.game_order[1], self.player2)

            self.game_order = []
            util.set_turn_helper(self.game_order, self.player, self.player2)
            self.assertEqual(self.game_order[0], self.player2)
            self.assertEqual(self.game_order[1], self.player)

    def test_isTokenValid(self):
        self.tokens = []
        result = util.isTokenValid("X", self.tokens)
        self.tokens.append("x")
        self.assertTrue(result)

        result = util.isTokenValid("X", self.tokens)
        self.assertFalse(result)

        result = util.isTokenValid(" ", self.tokens)
        self.assertFalse(result)

        result = util.isTokenValid("@", self.tokens)
        self.assertFalse(result)

        result = util.isTokenValid("1", self.tokens)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
