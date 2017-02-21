import unittest
from NaiveBayesClassifier import *


class TestNaiveBayes(unittest.TestCase):
    epsilon = 0.000001

    @classmethod
    def setUpClass(self):
        # self.b = NaiveBayesClassifier("input/double.txt")
        self.b = NaiveBayesClassifier()

    # @classmethod
    # def tearDownClass(self):

    def floatNotEquals(self, actual, expected):
        if((actual - expected) <= self.epsilon):
            self.fail("%f should not be near %f" % (actual, expected))

    def floatEquals(self, actual, expected):
        if((actual - expected) > self.epsilon):
            self.fail("%f is not near %f" % (actual, expected))

    def test_totals(self):
        self.floatEquals((self.b.positive + self.b.negative), 1)

if __name__ == '__main__':
    unittest.main()
