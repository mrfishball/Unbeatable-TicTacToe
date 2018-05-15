import unittest
from io import StringIO
from unittest import mock
from game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    # Test different input types to verify function correctly handles incorrect values
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_game_mode(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", "1", "4", "2", "99", "a", "@", "3"]):
            self.assertEqual(self.game.set_game_mode(), 1)
            self.assertEqual(self.game.set_game_mode(), 2)
            self.assertEqual(self.game.set_game_mode(), 3)

    #Test function applies strip() to user input before committing to any changes
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_players(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=[" ", " Lee", "John ", " Mary "]):
            self.game.set_players(1)
            self.assertEqual(self.game.player1.name, "Lee")
            self.assertEqual(self.game.player2.name, "Iris (AI)")

            self.game.set_players(2)
            self.assertEqual(self.game.player1.name, "John")
            self.assertEqual(self.game.player2.name, "Mary")

            self.game.set_players(3)
            self.assertEqual(self.game.player1.name, "Iris (AI)")
            self.assertEqual(self.game.player2.name, "Betty (AI)")

    #Tes two tokens should be unique and the fucntion handles incorrect or invalid token inputs
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_token(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=["a", "v", "V", "b"]):
            self.game.player1 = Human("Lee")
            self.game.player2 = Cpu("Iris (AI)")
            self.game.set_token(1, self.game.player1, self.game.player2)
            self.assertNotEqual(self.game.player1.token, self.game.player2.token)

            self.game.player1 = Human("John")
            self.game.player2 = Human("Mary")
            self.game.set_token(2, self.game.player1, self.game.player2)
            self.assertNotEqual(self.game.player1.token, self.game.player2.token)

            self.game.player1 = Cpu("Betty (AI)")
            self.game.player2 = Cpu("Iris (AI)")
            self.game.set_token(3, self.game.player1, self.game.player2)
            self.assertNotEqual(self.game.player1.token, self.game.player2.token)

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_turn(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=["3", "1", " ", "2", "a", "1",  "@", "2"]):
            self.game.game_order = []

            # Test when player chooses to go first, player should be the first item in game_order
            self.game.player1 = Human("John")
            self.game.player2 = Cpu("Iris (AI)")
            self.game.set_turn(1, self.game.player1, self.game.player2, self.game.game_order)
            self.assertEqual(self.game.game_order[0], self.game.player1)
            self.assertEqual(self.game.game_order[1], self.game.player2)

            # Test when player chooses to go first, player should be the last item in game_order
            self.game.game_order = []
            self.game.set_turn(1, self.game.player1, self.game.player2, self.game.game_order)
            self.assertEqual(self.game.game_order[0], self.game.player2)
            self.assertEqual(self.game.game_order[1], self.game.player1)

            # Test when the player who has the higher dice roll chooses to go first, that player should be the first item in game_order
            self.game.game_order = []
            self.game.player1 = Human("May")
            self.game.player2 = Human("Tony")
            self.game.set_turn(2, self.game.player1, self.game.player2, self.game.game_order)
            if self.game.player1.dice > self.game.player2.dice:

                self.assertEqual(self.game.game_order[0], self.game.player1)
                self.assertEqual(self.game.game_order[1], self.game.player2)
            else:
                self.assertEqual(self.game.game_order[0], self.game.player2)
                self.assertEqual(self.game.game_order[1], self.game.player1)

            # Test when the player has has higher dice roll chooses to go last, that player should be the last item in game_order
            self.game.game_order = []
            self.game.set_turn(2, self.game.player1, self.game.player2, self.game.game_order)
            if self.game.player1.dice > self.game.player2.dice:
                self.assertEqual(self.game.game_order[1], self.game.player1)
                self.assertEqual(self.game.game_order[0], self.game.player2)
            else:
                self.assertEqual(self.game.game_order[1], self.game.player2)
                self.assertEqual(self.game.game_order[0], self.game.player1)

    def test_get_opponent(self):
        self.game.player1 = Human("John")
        self.game.player2 = Cpu("Betty (AI)")

        opponent = self.game.get_opponent(self.game.player1)
        self.assertEqual(opponent, self.game.player2)

        opponent = self.game.get_opponent(self.game.player2)
        self.assertEqual(opponent, self.game.player1)

    def test_ifPlayerWin(self):
        board = Board()
        win_pattern = [
            ["X", "X", "X", 4, 5, 6, 7, 8, 9],
            [1, 2, 3, "X", "X", "X", 7, 8, 9],
            [1, 2, 3, 4, 5, 6, "X", "X", "X"],
            ["X", 2, 3, "X", 5, 6, "X", 8, 9],
            [1, "X", 3, 4, "X", 6, 7, "X", 9],
            [1, 2, "X", 4, 5, "X", 6, 7, "X"],
            ["X", 2, 3, 4, "X", 6, 7, 8, "X"],
            [1, 2, "X", 4, "X", 6, "X", 8, 9]
        ]
        player = Human("Tony")
        player.set_token("X")

        for pattern in win_pattern:
            with self.subTest(pattern = pattern):
                board.board = pattern
                result = self.game.ifPlayerWin(board, player)
                self.assertTrue(result)

        # board.board = ["X", "X", "X", 4, 5, 6, 7, 8, 9]
        # result = self.game.ifPlayerWin(board, player)
        # self.assertTrue(result)
        #
        # board.board = [1, 2, 3, "X", "X", "X", 7, 8, 9]
        # result = self.game.ifPlayerWin(board, player)
        # self.assertTrue(result)
        #
        # board.board = [1, 2, 3, 4, 5, 6, "X", "X", "X"]
        # result = self.game.ifPlayerWin(board, player)
        # self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
