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
    prev = list(range(len(b) + 1))
    for i, xa in enumerate(a, start=1):
        curr = [i] + [0] * len(b)
        for j, xb in enumerate(b, start=1):
            cost = 0 if abs(xa - xb) <= tol else 1
            curr[j] = min(
                prev[j] + 1,        # deletion
                curr[j - 1] + 1,    # insertion
                prev[j - 1] + cost  # substitution / match
            )
        prev = curr
    return prev[-1]


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
    m, n = len(a), len(b)
    dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0.0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0.0 if a[i - 1] == b[j - 1] else 1.0
            dp[i][j] = cost + min(
                dp[i - 1][j],     # stretch a (repeat a[i-1])
                dp[i][j - 1],     # stretch b (repeat b[j-1])
                dp[i - 1][j - 1]  # advance both
            )
    return dp[m][n]


# ANSWER 1: (the QUESTION is at the top of this file)

# ANSWER 2: (the QUESTION is at the top of this file)
