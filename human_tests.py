import unittest
from human import *

class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human = Human("Tom")
        self.human2 = Human("Mary")

    def test_init(self):
        self.assertEqual(self.human.name, "Tom")
        self.assertEqual(self.human2.name, "Mary")
        self.assertEqual(self.human.token, None)
        self.assertEqual(self.human2.token, None)


if __name__ == '__main__':
    unittest.main()
