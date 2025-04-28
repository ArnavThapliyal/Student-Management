"""
Unit tests for validation functions.
"""

import unittest
from validation import validate_roll, validate_email
class TestValidation(unittest.TestCase):

    def test_validate_roll(self):
        self.assertTrue(validate_roll("AB12CD345"))
        self.assertFalse(validate_roll("AB1234CD5"))
        self.assertFalse(validate_roll("abcd12345"))

    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("test@.com"))
        self.assertFalse(validate_email("test@com"))

if __name__ == '__main__':
    unittest.main()
