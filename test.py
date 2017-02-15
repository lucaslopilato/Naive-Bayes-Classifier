import unittest
from FileParser import *


class TestFileParser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.p = FileParser('input/testing.txt')

    @classmethod
    def tearDownClass(self):
        self.p.__del__

    def test_blacklist(self):
        self.assertNotIn('luke', self.p.blacklist)
        self.assertIn('the', self.p.blacklist)
        self.assertIn('and', self.p.blacklist)

    def test_cleanse(self):
        self.assertEqual(self.p.cleanse("123512*&^^%@$!@^*&"), {})
        self.assertEqual(self.p.cleanse("ron"), {'ron': 1})
        self.assertEqual(self.p.cleanse("12 rom 45 molem 4()"),
            {'rom': 1, 'molem': 1})

    def test_cleanseNegation(self):
        self.assertEqual(self.p.cleanse("not not not not not"), {})
        self.assertEqual(self.p.cleanse("not not not not not me"), {'me': -1})
        self.assertEqual(self.p.cleanse("not not not not me"), {'me': 1})
        self.assertEqual(self.p.cleanse("not not tim not not not me"),
            {'tim': 1, 'me': -1})


if __name__ == '__main__':
    unittest.main()
