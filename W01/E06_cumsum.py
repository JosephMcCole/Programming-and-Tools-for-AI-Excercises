"""Drill. The accumulator pattern.

Run the tests:

    python -m doctest W01/E06_cumsum.py

No output means every test passed.
"""


def cumsum(L):
    """Return the cumulative sum of L. A tuple input still returns a list.

    >>> cumsum([1, 2, 3])
    [1, 3, 6]
    >>> cumsum([5, 5, 5])
    [5, 10, 15]
    >>> cumsum([])
    []
    >>> cumsum([5])
    [5]
    >>> cumsum((5, 5, 5))
    [5, 10, 15]
    """
    result = []#adding a result list to add the total to
    total = 0#declaring variable total and starting it at 0 to allow use in the for loop
    for i in L:#iterating over the input L
        total += i#adding each item in L to the total
        #in this stage of the for loop the current value of total is added to the result list
        result.append(total)
    return result    
            
