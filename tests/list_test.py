import unittest
import list


class TestList(unittest.TestCase):
    def test_key_exists(self):
        """
        Tests key existence in dictionary.
        """
        testdata = {
            'foo': 'bar',
            'baz': 'foo'
        }

        self.assertTrue(list.key_exists('foo', testdata))
        self.assertFalse(list.key_exists('bar', testdata))

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

        result = list.decode_elements(testdata)

        for data in result:
            self.assertEqual(data, 'test data')


if __name__ == '__main__':
    unittest.main()
