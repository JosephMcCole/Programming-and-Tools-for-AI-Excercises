"""Drill. Slicing.

Run the tests:

    python -m doctest W01/E03_slices.py

No output means every test passed.
"""


def middle(s):
    """Return everything except the first and last item.

    >>> middle("hello")
    'ell'
    >>> middle("ab")
    ''
    >>> middle([1, 2, 3, 4])
    [2, 3]
    """
    return s[1:-1]#-1 at the end is non inclusive when it is the second item in the slice, so it will not include the last item in the slice


def last_three(s):
    """Return the last three items. If there are fewer, return them all.

    >>> last_three("hello")
    'llo'
    >>> last_three("hi")
    'hi'
    >>> last_three([1, 2, 3, 4, 5])
    [3, 4, 5]
    """
    return s[-3:]#-3 is the starting index for the slice, and : means go to the end of the input list
