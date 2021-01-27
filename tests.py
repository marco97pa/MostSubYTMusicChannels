import unittest

from main import gen_hashtags


class GenHashtags(unittest.TestCase):
    """
        Tests that it can generate valid hashtags
    """
    def test_single_name(self):
        """ Simple test with an artist with only a name """ 
        result = gen_hashtags("BLACKPINK")
        self.assertEqual(result, "#music #youtube #stats #blackpink")

    def test_double_name(self):
        """ Test with an artist with name and surname """
        result = gen_hashtags("Dua Lipa")
        self.assertEqual(result, "#music #youtube #stats #dualipa #dua #lipa")

    def test_numeric_name(self):
        """ Test with an artist which name contains a number """
        result = gen_hashtags("Maroon 5")
        self.assertEqual(result, "#music #youtube #stats #maroon5 #maroon")

if __name__ == '__main__':
    unittest.main()