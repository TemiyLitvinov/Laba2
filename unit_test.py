import unittest
from check_password import is_valid_password

class TestPasswordRegex(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(is_valid_password("OKPassword321$"))

    def test_no_uppercase(self):
        self.assertFalse(is_valid_password("badpassword5729*"))

    def test_no_lowercase(self):
        self.assertFalse(is_valid_password("BIGPASSWORD*7843"))

    def test_no_digit(self):
        self.assertFalse(is_valid_password("NoDigitsPassword$"))

    def test_no_special(self):
        self.assertFalse(is_valid_password("CommonPassword#"))

    def test_short(self):
        self.assertFalse(is_valid_password("tooShort2&"))

    def test_with_space(self):
        self.assertFalse(is_valid_password("Hello world!341"))

    def test_long_valid(self):
        self.assertTrue(is_valid_password("GoodPassword3748@"))

if __name__ == "__main__":
    unittest.main()