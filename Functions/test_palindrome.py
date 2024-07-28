
# test_palindrome.py
import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("oso"))
        self.assertFalse(is_palindrome("python"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("anita lava la tina"))
        self.assertFalse(is_palindrome("esto no es un palindromo"))

    def test_palindrome_case_insensitive(self):
        self.assertTrue(is_palindrome("Oso"))
        self.assertTrue(is_palindrome("RaDaR"))

    def test_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_palindrome_single_character(self):
        self.assertTrue(is_palindrome("a"))

if __name__ == '__main__':
    unittest.main()