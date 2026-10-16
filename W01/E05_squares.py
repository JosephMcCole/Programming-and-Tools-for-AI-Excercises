"""Drill. Building a list with append.

Run the tests:

    python -m doctest W01/E05_squares.py

No output means every test passed.
"""


def squares(n):
    """Return a list of the squares of 1 up to and including n.

    >>> squares(4)
    [1, 4, 9, 16]
    >>> squares(1)
    [1]
    >>> squares(0)
    []
    """
    newListOfSquares = []#a list here as it will be appended to later to store the squares
    #loop through numbers 1 to n 
    #When the squares function calls squares(0) the range is (1,1) so the list is empty and does not run
    for i in range(1, n + 1):
        #adding the i**2 squared notation to the list of squares
        newListOfSquares.append(i**2)
    return newListOfSquares
