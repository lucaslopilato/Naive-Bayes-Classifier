import unittest
from FileParser import *


class TestFileParser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.p = FileParser('testing.txt')

    @classmethod
    def tearDownClass(self):
        self.p.__del__

    def test_blacklist(self):
        self.assertNotIn('luke', self.p.blacklist)
        self.assertIn('the', self.p.blacklist)
        self.assertIn('and', self.p.blacklist)

    def test_nontext(self):
        self.assertEqual(self.p.cleanse("123512*&^^%@$!@^*&"), {})


if __name__ == '__main__':
    unittest.main()
