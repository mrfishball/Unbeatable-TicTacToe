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
        print("Testing game mode selection...")
        with mock.patch("builtins.input", side_effect=[" ", "1", "4", "2", "99", "a", "@", "3"]):
            self.assertEqual(self.game.set_game_mode(), 1)
            self.assertEqual(self.game.set_game_mode(), 2)
            self.assertEqual(self.game.set_game_mode(), 3)
        print("Passed!")

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
            player1 = Human("Lee")
            player2 = Cpu("Iris (AI)")
            self.game.set_token(1, player1, player2)
            self.assertNotEqual(player1.token, player2.token)

            player1 = Human("John")
            player2 = Human("Mary")
            self.game.set_token(2, player1, player2)
            self.assertNotEqual(player1.token, player2.token)

            player1 = Cpu("Betty (AI)")
            player2 = Cpu("Iris (AI)")
            self.game.set_token(3, player1, player2)
            self.assertNotEqual(player1.token, player2.token)

    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_set_turn(self, mock_stdout):
        with mock.patch("builtins.input", side_effect=["3", "1", " ", "2", "a", "1",  "@", "2"]):
            game_order = []

            # Test when player chooses to go first, player should be the first item in game_order
            player1 = Human("John")
            player2 = Cpu("Iris (AI)")
            self.game.set_turn(1, player1, player2, game_order)
            self.assertEqual(game_order[0], player1)
            self.assertEqual(game_order[1], player2)

            # Test when player chooses to go first, player should be the last item in game_order
            game_order = []
            self.game.set_turn(1, player1, player2, game_order)
            self.assertEqual(game_order[0], player2)
            self.assertEqual(game_order[1], player1)

            # Test when the player who has the higher dice roll chooses to go first, that player should be the first item in game_order
            game_order = []
            player1 = Human("May")
            player2 = Human("Tony")
            self.game.set_turn(2, player1, player2, game_order)
            if player1.dice > player2.dice:
                self.assertEqual(game_order[0], player1)
                self.assertEqual(game_order[1], player2)
            else:
                self.assertEqual(game_order[0], player2)
                self.assertEqual(game_order[1], player1)

            # Test when the player has has higher dice roll chooses to go last, that player should be the last item in game_order
            game_order = []
            self.game.set_turn(2, player1, player2, game_order)
            if player1.dice > player2.dice:
                self.assertEqual(game_order[1], player1)
                self.assertEqual(game_order[0], player2)
            else:
                self.assertEqual(game_order[1], player2)
                self.assertEqual(game_order[0], player1)

    # Test that the function to correctly detect win patterns
    def test_ifPlayerWin(self):
        board = Board()
        player = Human("Tony")
        player.token = "X"
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

        for pattern in win_pattern:
            with self.subTest(pattern = pattern):
                board.board = pattern
                result = self.game.ifPlayerWin(board, player)
                self.assertTrue(result)

    # Test that the function detects ties correctly
    def test_tie(self):
        board = Board()
        player = Human("Tony")
        player.token = "X"
        player2 = Human("Mary")
        player2.token = "O"

        patterns = [
            ["X", "O", "X", "X", "O", "X", "O", "X", "O"],
            ["X", "O", "O", "O", "O", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "O", "O", "O", "X", "X"]
        ]

        for pattern in patterns:
            with self.subTest(pattern = pattern):
                board.board = pattern
                result = self.game.tie(board, player, player2)
                self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
