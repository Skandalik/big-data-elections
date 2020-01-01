import unittest
import normalizer
import os


class TestNormalizer(unittest.TestCase):
    def test_sanitize(self):
        """
        Tests sanitization of tweets from deleted tweets.
        """
        tweets = [
            {"delete": 1},
            {"created_at": "12.04.2019"},
            {"different_key": "test", "delete": 1},
        ]

        normalizer.sanitize(tweets)
        self.assertEqual(len(tweets), 1)

    def test_key_exists(self):
        """
        Tests key existence in dictionary.
        """
        testdata = {
            'foo': 'bar',
            'baz': 'foo'
        }

        self.assertTrue(normalizer.__key_exists__('foo', testdata))
        self.assertFalse(normalizer.__key_exists__('bar', testdata))

    def test_strip_elements(self):
        """
        Tests trimming whitespace from list elements.
        """
        testdata = [
            'test data  \n',
            'test data ',
            '     test data ',
            'test data',
        ]

        result = normalizer.__strip_elements__(testdata)

        for data in result:
            self.assertEqual(data, 'test data')

    def test_get_tweets(self):
        """
        Tests getting data from a file.
        """

        filepath = '%s\\testdata\\tweets.json' % os.getcwd()
        result = normalizer.__get_tweets__(filepath)

        self.assertEqual(len(result), 9)


if __name__ == '__main__':
    unittest.main()
