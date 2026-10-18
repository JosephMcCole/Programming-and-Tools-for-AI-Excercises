"""Composition. Rotation, in one line, with slicing.

Run the tests:

    python -m doctest W01/E11_rotate.py

No output means every test passed.
"""


def rotate(s, k):
    """Move the first k items of s to the end.

    This is the trick that made the cipher easy in the lecture. It works on
    a list as well as a string. If k is bigger than s, wrap around.

    >>> rotate("abcdef", 2)
    'cdefab'
    >>> rotate("abcdef", 0)
    'abcdef'
    >>> rotate([1, 2, 3, 4], 1)
    [2, 3, 4, 1]
    >>> rotate("abc", 3)
    'abc'
    >>> rotate("abc", 4)
    'bca'
    >>> rotate("", 2)
    ''
    """
    #using check for zero value logic here and just returning the empty value if it is empty
    if len(s) == 0:
        return s
    else:
        #assignment of k to be the remainder of k divided by the length of s
        #this is done as to slice the list/string at a value of k in the return
        #statement
        k = k % len(s)
    return s[k:] + s[:k]#returning the sliced values added together