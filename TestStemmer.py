import unittest
from stemmer import *

class TestStemmer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.s = stemmer()

    def test_vowels(self):
        word = 'toy'
        self.assertFalse(self.s.isVowel(word, 0))
        self.assertTrue(self.s.isVowel(word, 1))
        self.assertFalse(self.s.isVowel(word, 2))

        word = 'syzygy'
        self.assertFalse(self.s.isVowel(word, 0))
        self.assertFalse(self.s.isVowel(word, 2))
        self.assertFalse(self.s.isVowel(word, 4))
        self.assertTrue(self.s.isVowel(word, 1))
        self.assertTrue(self.s.isVowel(word, 3))
        self.assertTrue(self.s.isVowel(word, 5))

    def test_measure(self):
        self.assertEqual(self.s.measure('tr'), 0)
        self.assertEqual(self.s.measure('ee'), 0)
        self.assertEqual(self.s.measure('tree'), 0)
        self.assertEqual(self.s.measure('y'), 0)
        self.assertEqual(self.s.measure('by'), 0)

        self.assertEqual(self.s.measure('trouble'), 1)
        self.assertEqual(self.s.measure('oats'), 1)
        self.assertEqual(self.s.measure('trees'), 1)
        self.assertEqual(self.s.measure('ivy'), 1)

        self.assertEqual(self.s.measure('troubles'), 2)
        self.assertEqual(self.s.measure('private'), 2)
        self.assertEqual(self.s.measure('oaten'), 2)
        self.assertEqual(self.s.measure('orrery'), 2)

    def test_hasVowel(self):
        self.assertTrue(self.s.containsVowel('eatery'))
        self.assertFalse(self.s.containsVowel('ttmlpq'))

    def test_onea(self):
        self.assertEqual(self.s.stepone('caresses'), 'caress')
        self.assertEqual(self.s.stepone('ponies'), 'poni')
        self.assertEqual(self.s.stepone('caress'), 'caress')
        self.assertEqual(self.s.stepone('cats'), 'cat')
        self.assertEqual(self.s.stepone('feed'), 'feed')
        self.assertEqual(self.s.stepone('agreed'), 'agree')
        self.assertEqual(self.s.stepone('plastered'), 'plaster')
        self.assertEqual(self.s.stepone('bled'), 'bled')
        self.assertEqual(self.s.stepone('motoring'), 'motor')
        self.assertEqual(self.s.stepone('sing'), 'sing')

    def test_doubleconst(self):
        self.assertFalse(self.s.doubleConst('ea'))
        self.assertFalse(self.s.doubleConst('ba'))
        self.assertFalse(self.s.doubleConst('ab'))
        self.assertTrue(self.s.doubleConst('tt'))
        self.assertTrue(self.s.doubleConst('arnett'))







if __name__ == '__main__':
    unittest.main()