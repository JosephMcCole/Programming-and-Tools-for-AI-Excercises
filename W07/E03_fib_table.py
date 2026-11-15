"""Drill. Fibonacci from the bottom up.

Run the tests:

    python -m doctest W07/E03_fib_table.py

No output means every test passed.

The lecture's `fib_slow` is exponential because it asks the same questions over
and over. Fill a table instead, smallest first, so each answer is computed
once. Then notice how little of that table you actually needed.
"""
def fib_table(n):
    """Return the nth Fibonacci number, building a list from the bottom up.

    >>> [fib_table(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fib_table(35)
    9227465
    """
    #start at zero and one, the first two fib numbers
    table = [0, 1]
    #_ as we do not need a loop counter in the loop
    for _ in range(2, n + 1):
        table.append(table[-1] + table[-2])
    #return the final answer at index n
    return table[n]


def fib_pair(n):
    """The same answer, keeping only the two values we still need.

    >>> [fib_pair(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fib_pair(35)
    9227465
    >>> all(fib_pair(i) == fib_table(i) for i in range(50))
    True
    """
    #tracks the two most recent cases and it will not lookfuther backe than 0 and 1
    a, b = 0, 1
    #again not not need a loop counter in the loop
    for _ in range(n):
    #advance both values in the fib sequence
        a, b = b, a + b
    #return the a value
    return a


# `fib_table` holds n numbers to return one. `fib_pair` holds two. This is the
# same saving we make for edit distance in E05, one dimension down: look at the
# recurrence, see how far back it actually reaches, and keep only that much.
