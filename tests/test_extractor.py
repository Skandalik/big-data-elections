import unittest
import extractor
import os


class TestExtractor(unittest.TestCase):
    def test_extract_tweets(self):
        to_extract: list = [
            '{"delete": "true"}',
            '{"delete": {"foo": "bar"}}',
            '{"updated_at": "21:37"}',
            '{"updated_at": "21:37","delete": "true"}'
        ]

        extracted = extractor.create().extract_tweets(to_extract)
        self.assertEqual(len(extracted), 1)


if __name__ == '__main__':
    unittest.main()
