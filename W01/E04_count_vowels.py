"""Drill. Looping over a string.

Run the tests:

    python -m doctest W01/E04_count_vowels.py

No output means every test passed.
"""


def count_vowels(s):
    """Return the number of vowels in s. Upper case counts too.

    >>> count_vowels("hello")
    2
    >>> count_vowels("xyz")
    0
    >>> count_vowels("AEIOU")
    5
    >>> count_vowels("")
    0
    """
    return sum(1 for c in s if c.lower() in "aeiou")
