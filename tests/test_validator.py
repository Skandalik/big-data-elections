import unittest
import validator


class TestValidator(unittest.TestCase):
    def test_validate_valid(self):
        data = {
            "foo": "bar,"
        }

        self.assertTrue(validator.create().validate(data))

    def test_validate_invalid(self):
        data = {
            "delete": True,
            "foo": "bar,"
        }

        self.assertFalse(validator.create().validate(data))


if __name__ == '__main__':
    unittest.main()
