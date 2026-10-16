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
    count = 0#declare a count variable 
    for c in s:#a for loop to iterate over the input
        if c.lower() in "aeiou":
            #use .lower function to allow for the if statement to account for capital letters
            count += 1#add to count 1 if the above c variable is in aeiou
    return count#return the total number of vowels