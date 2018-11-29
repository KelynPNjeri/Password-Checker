"""Tests Module."""
import unittest
from ddt import ddt, data
from password_checker import validate_password

@ddt
class TestPasswordChecker(unittest.TestCase):
    """
    Testing the Password Checker.
    """
    def setUp(self):
        """setUp Method"""
        self.valid_password = "Example@1998"
    def test_valid_password(self):
        """
        Testing a valid password."""
        result = validate_password(self.valid_password)
        self.assertEqual(result, "Valid Password")

    @data(
        " ",
        "Exam",
        "example@1998",
        "Example123",
        "Example",
        "Exampleisreallylong",
    )
    def test_invalid_password(self, value):
        """
        Testing Invalid Passwords.
        """
        result = validate_password(value)
        self.assertEqual(result, "Invalid Password")

    def tearDown(self):
        self.valid_password = None

if __name__ == "__main__":
    unittest.main()
