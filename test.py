import unittest
from FileParser import *


class TestFileParser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.instance = FileParser('testing.txt')

    @classmethod
    def tearDownClass(self):
        self.instance.__del__

    def test_blacklist(self):
        self.assertNotIn('luke', self.instance.blacklist)
        self.assertIn('the', self.instance.blacklist)
        self.assertIn('and', self.instance.blacklist)

    def test_nontext(self):
        self.assertEqual(self.instance.cleanse("123512*&^^%@$!@^*&"), {})


if __name__ == '__main__':
    unittest.main()
