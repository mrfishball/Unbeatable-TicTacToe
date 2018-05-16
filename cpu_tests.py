import unittest
from unittest import mock
from io import StringIO
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
        pass

    def test_best_move(self):
        # Test if the AI can make a move to block the opponent from winning
        pattern = ["X", "X", "O", 4, "O", 6, 7, 8, 9]
        self.board.board = pattern
        result = self.cpu.best_move(self.board, self.cpu, self.cpu)[0]
        self.assertEqual(result, 6)

        # Test if the AI can make a winning move
        pattern2 = ["X", "O", "O", "O", "X", 6, 7, 8, 9]
        self.board.board = pattern2
        result = self.cpu.best_move(self.board, self.cpu, self.cpu)[0]
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
