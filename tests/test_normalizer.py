import unittest
import normalizer
import os


class TestNormalizer(unittest.TestCase):
    def test_normalize(self):
        filepath = '%s\\..\\testdata\\tweets.json' % os.getcwd()

        normalized = normalizer.create(filepath).normalize()
        self.assertEqual(len(normalized), 7)

    def test_normalize_nested(self):
        filepath = '%s\\..\\testdata\\nested' % os.getcwd()

        normalized = normalizer.create(filepath).normalize()
        self.assertEqual(len(normalized), 73)


if __name__ == '__main__':
    unittest.main()
