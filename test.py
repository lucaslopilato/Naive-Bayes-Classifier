import unittest
from NaiveBayesClassifier import *


class TestFileParser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.p = FileParser('input/testing.txt')
        self.t = TrainingParser('input/training.txt')
        self.b = NaiveBayesClassifier()

    @classmethod
    def tearDownClass(self):
        self.p.__del__
        self.t.__del__

    def test_mainInit(self):
        # Test Data Handoff from FileParser
        self.assertEqual(len(self.b.train), 5000)
        self.assertEqual(self.b.rating[0], 1)
        self.assertEqual(self.b.rating[4999], 1)
        self.assertEqual(self.b.rating[2], 0)

        # Test Class Counts
        self.assertEqual(self.b.ndocs + self.b.pdocs, 5000)

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
            self.assertEqual(len(self.t.train), 5000)
            # Test Stop Words
            self.assertNotIn('the', self.t.train[0])
            self.assertNotIn('to', self.t.train[0])
            self.assertNotIn('that', self.t.train[0])
            self.assertNotIn('of', self.t.train[0])
            self.assertNotIn('is', self.t.train[0])
            self.assertNotIn('i', self.t.train[0])
            self.assertNotIn('a', self.t.train[0])
            self.assertNotIn('their', self.t.train[0])
            self.assertNotIn('my', self.t.train[0])
            self.assertNotIn('me', self.t.train[0])
            self.assertNotIn('it', self.t.train[0])
            self.assertNotIn('it', self.t.train[0])
            self.assertNotIn('at', self.t.train[0])
            self.assertNotIn('as', self.t.train[0])
            self.assertNotIn('your', self.t.train[0])
            self.assertNotIn('who', self.t.train[0])
            self.assertNotIn('which', self.t.train[0])
            self.assertNotIn('when', self.t.train[0])
            self.assertNotIn('what', self.t.train[0])

            # Test Things that should be in the first review
            self.assertIn('high', self.t.train[0])
            self.assertIn('bromwell', self.t.train[0])
            self.assertIn('teachers', self.t.train[0])
            self.assertIn('student', self.t.train[0])
            self.assertIn('students', self.t.train[0])
            self.assertIn('school', self.t.train[0])
            self.assertIn('school', self.t.train[0])
            self.assertIn('welcome', self.t.train[0])
            self.assertIn('tried', self.t.train[0])
            self.assertIn('time', self.t.train[0])
            self.assertIn('think', self.t.train[0])
            self.assertIn('teaching', self.t.train[0])
            self.assertIn('survive', self.t.train[0])
            self.assertIn('teachers', self.t.train[0])

if __name__ == '__main__':
    unittest.main()
