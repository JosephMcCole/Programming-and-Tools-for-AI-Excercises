"""Extension. Each algorithm on the other one's data.

Run the tests:

    python -m doctest W07/E06_wrong_tool.py

No output means every test passed.

Levenshtein is for symbols and DTW is for numbers. Nothing stops you running
either on the other kind of data, and what goes wrong is worth understanding:
each algorithm has an assumption built into it, and the assumption only shows
itself when it is false.

Write both functions, then answer the questions from what the doctests show.

QUESTION 1: `levenshtein` compares items with `==`, and two measured floats are
almost never exactly equal. What does the distance degenerate to? Does `tol`
really fix it?

QUESTION 2: `dtw_symbols("bookkeeper", "bokeper")` is 0.0, meaning DTW calls
the misspelling a perfect match. Explain why, and say whether DTW could ever be
used for spellchecking. Write your answers in the comments at the bottom.
"""

INF = float("inf")


def levenshtein_tol(a, b, tol):
    """Edit distance on numbers, counting two values equal if within tol.

    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], 0.0)
    0
    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.05, 2.0, 3.0], 0.0)
    1
    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.05, 2.0, 3.0], 0.1)
    0
    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.0, 1.0, 2.0, 3.0], 0.1)
    1
    >>> levenshtein_tol([1.0], [999.0], 0.1)
    1
    """
    return  # YOUR CODE HERE


def dtw_symbols(a, b):
    """DTW on symbols, costing 0 for a match and 1 for a mismatch.

    >>> dtw_symbols("abc", "abc")
    0.0
    >>> dtw_symbols("abc", "xyz")
    3.0
    >>> dtw_symbols("aab", "ab")
    0.0
    >>> dtw_symbols("bookkeeper", "bokeper")
    0.0
    """
    return  # YOUR CODE HERE


# ANSWER 1: (the QUESTION is at the top of this file)

# ANSWER 2: (the QUESTION is at the top of this file)
