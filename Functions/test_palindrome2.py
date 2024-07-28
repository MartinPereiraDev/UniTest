# functions.py
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

def sum(a, b):
    return a + b

# test_functions.py
import pytest
from test_palindrome2 import is_palindrome, sum

def test_palindrome_simple():
    assert is_palindrome("radar")
    assert is_palindrome("oso")
    assert not is_palindrome("python")

def test_palindrome_with_spaces():
    assert is_palindrome("anita lava la tina")
    assert not is_palindrome("esto no es un palindromo")

def test_palindrome_case_insensitive():
    assert is_palindrome("Oso")
    assert is_palindrome("RaDaR")

def test_palindrome_empty_string():
    assert is_palindrome("")

def test_palindrome_single_character():
    assert is_palindrome("a")

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 20, 30),
    (-1, -2, -3),
    (-10, 5, -5),
    (0, 0, 0),
    (10, 0, 10),
    (0, -5, -5)
])
def test_sum(a, b, expected):
    assert sum(a, b) == expected