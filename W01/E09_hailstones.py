"""Composition. Hailstone sequences.

Run the tests:

    python -m doctest W01/E09_hailstones.py

No output means every test passed.
"""


def hailstones(n):
    """Return the hailstone sequence starting at n and ending at 1.

    If n is even, the next number is n/2. If n is odd, it is 3n+1.

    >>> hailstones(1)
    [1]
    >>> hailstones(10)
    [10, 5, 16, 8, 4, 2, 1]
    >>> hailstones(7)[:6]
    [7, 22, 11, 34, 17, 52]
    >>> len(hailstones(27))
    112
    """
    return  


def longest_hailstone(limit):
    """Return (n, length) for the longest hailstone sequence with n < limit.

    >>> longest_hailstone(10)
    (9, 20)
    >>> longest_hailstone(100)
    (97, 119)
    >>> longest_hailstone(1000)
    (871, 179)
    """
    return  # YOUR CODE HERE
