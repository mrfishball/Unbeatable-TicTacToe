import unittest
from cpu import *
from board import *

class TestCpu(unittest.TestCase):

    def setUp(self):
        self.cpu = Cpu("Betty")
        self.cpu.token = "X"
        self.cpu2 = Cpu("Dave")
        self.cpu2.token = "O"

        self.cpu.opponent = self.cpu2
        self.cpu2.opponent = self.cpu

        self.board = Board()

    def test_make_a_move(self):

        # Test that the function returns the correct move generated and that it's
        # being registered to the board
        pattern = ["O", "O", "X", 4, "X", 6, 7, 8, 9]
        self.board.board = pattern
        result = self.cpu2.make_a_move(self.board)
        self.assertEqual(result, 7)
        self.assertEqual(self.board.board[result-1], self.cpu2.token)

        pattern = ["X", "O", "O", "O", "X", 6, 7, 8, 9]
        self.board.board = pattern
        result = self.cpu2.make_a_move(self.board)
        self.assertEqual(result, 9)
        self.assertEqual(self.board.board[result-1], self.cpu2.token)

    def test_best_move(self):
        # Test if the AI can make a move to block the opponent from winning
        # Test that it should not make the move permanent as that's
        # handled by make_a_move
        pattern = ["X", "X", "O", 4, "O", 6, 7, 8, 9]
        self.board.board = pattern
        result = self.cpu.best_move(self.board, self.cpu, self.cpu)[0]
        self.assertEqual(result, 6)
        self.assertNotEqual(self.board.board[result-1], self.cpu.token)

        # Test if the AI can make a winning move
        # Test that it should not make the move permanent as that's
        # handled by make_a_move
        pattern = ["X", "O", "O", "O", "X", 6, 7, 8, 9]
        self.board.board = pattern
        result = self.cpu.best_move(self.board, self.cpu, self.cpu)[0]
        self.assertEqual(result, 8)
        self.assertNotEqual(self.board.board[result-1], self.cpu.token)

if __name__ == '__main__':
    unittest.main()
