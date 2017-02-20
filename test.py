import unittest
from NaiveBayesClassifier import *


class TestFileParser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.b = NaiveBayesClassifier()
        self.p = FileParser()
        self.epsilon = 0.000001

    # @classmethod
    # def tearDownClass(self):

    def floatEquals(self, actual, expected):
        if((actual - expected) > self.epsilon):
            self.fail("%f is not near %f" % (actual, expected))

    def test_mainInit(self):
        # Test Data Handoff from FileParser
        self.assertEqual(len(self.b.train), 5000)
        self.assertEqual(self.b.rating[0], 1)
        self.assertEqual(self.b.rating[4999], 1)
        self.assertEqual(self.b.rating[2], 0)

        # Test Class Counts
        # self.assertEqual(len(self.b.positive) + len(self.b.negative), 5000)

    def test_blacklist(self):
        self.assertNotIn('luke', self.p.stop)
        self.assertIn('the', self.p.stop)
        self.assertIn('and', self.p.stop)

    def test_cleanse(self):
        self.assertEqual(self.p.cleanse("123512*&^^%@$!@^*&"), {})
        self.assertEqual(self.p.cleanse("ron"), {'ron': 1})
        self.assertEqual(self.p.cleanse("12 rom 45 molem 4()"),
            {'rom': 1, 'molem': 1})

    '''def test_cleanseNegation(self):
        self.assertEqual(self.p.cleanse("not not not not not"), {})
        self.assertEqual(self.p.cleanse("not not not not not funny"), {'funny': -1})
        self.assertEqual(self.p.cleanse("not not not not funny"), {'funny': 1})
        self.assertEqual(self.p.cleanse("not not tim not not not funny"),
            {'tim': 1, 'funny': -1})'''

    def test_cleanseFile(self):
            train = self.p.getReviews('input/training.txt')
            self.assertEqual(len(train), 5000)
            # Test Stop Words
            self.assertNotIn('the', train[0])
            self.assertNotIn('to', train[0])
            self.assertNotIn('that', train[0])
            self.assertNotIn('of', train[0])
            self.assertNotIn('is', train[0])
            self.assertNotIn('i', train[0])
            self.assertNotIn('a', train[0])
            self.assertNotIn('their', train[0])
            self.assertNotIn('my', train[0])
            self.assertNotIn('me', train[0])
            self.assertNotIn('it', train[0])
            self.assertNotIn('it', train[0])
            self.assertNotIn('at', train[0])
            self.assertNotIn('as', train[0])
            self.assertNotIn('your', train[0])
            self.assertNotIn('who', train[0])
            self.assertNotIn('which', train[0])
            self.assertNotIn('when', train[0])
            self.assertNotIn('what', train[0])
            self.assertNotIn('teachers', train[0])
            self.assertNotIn('students', train[0])

            # Test Things that should be in the first review
            self.assertIn('high', train[0])
            self.assertIn('bromwell', train[0])
            self.assertIn('student', train[0])
            self.assertIn('school', train[0])
            self.assertIn('school', train[0])
            self.assertIn('welcome', train[0])
            # self.assertIn('tried', train[0])
            self.assertIn('time', train[0])
            self.assertIn('think', train[0])
            self.assertIn('teach', train[0])
            self.assertIn('survive', train[0])

    def test_accuracy(self):
        expected = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
        actual = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1]
        acc = self.b.accuracy(expected, actual)
        self.floatEquals(acc, 1)

    def test_destem(self):
        self.assertEqual("stem", self.p.destem("stems"))
        self.assertEqual("stem", self.p.destem("stemming"))
        self.assertEqual("stem", self.p.destem("stemmed"))
        self.assertEqual("teach", self.p.destem("teacher"))
        self.assertEqual("teach", self.p.destem("teaching"))

if __name__ == '__main__':
    unittest.main()
