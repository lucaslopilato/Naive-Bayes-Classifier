import unittest
from Trainer import *


class TestTrainer(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.single = Trainer('input/single.txt')
        self.full = Trainer('input/training.txt')

    def test_singleReadin(self):
        self.assertEqual(self.single.positiveDocs, 1)
        self.assertEqual(self.single.negativeDocs, 0)
        self.assertEqual(len(self.single.negativeWords), 0)
        self.assertEqual(len(self.single.positiveWords), 90)


if __name__ == '__main__':
    unittest.main()
