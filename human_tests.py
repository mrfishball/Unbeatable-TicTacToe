import unittest
from human import *

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human = Human("Tom")
        self.human2 = Human("Mary")

    def test_init(self):
        self.assertEqual(self.human.name, "Tom")
        self.assertEqual(self.human2.name, "Mary")
        self.assertEqual(self.human.opponent, None)
        self.assertEqual(self.human2.opponent, None)
        self.assertEqual(self.human.token, None)
        self.assertEqual(self.human2.token, None)

    def test_opponent(self):
        self.human.opponent = self.human2
        self.human2.opponent = self.human
        self.assertEqual(self.human.opponent, self.human2)
        self.assertEqual(self.human2.opponent, self.human)


if __name__ == '__main__':
    unittest.main()
