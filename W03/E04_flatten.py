"""Drill. The same walk, collecting instead of adding.

Run the tests:

    python -m doctest W03/E04_flatten.py

No output means every test passed.
"""


def flatten(items):
    """Return a flat list of every number in items, in the order they appear.

    Same two cases as nested_sum. The only difference is what you do with
    the answer from below: append adds one item, extend adds all the items
    of another list.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([1, [2, 3], [4, [5]]])
    [1, 2, 3, 4, 5]
    >>> flatten([])
    []
    >>> flatten([[], [[]]])
    []
    >>> flatten([[[[7]]]])
    [7]
    """
    result = []
    for item in items:
        #identifies if the item in items is a list or not
        if isinstance(item, list):
            #here the list is dissolved by the extend flatten functionality
            result.extend(flatten(item))
        else:
            #if the item is not a list it appends it
            result.append(item)

    return result  
