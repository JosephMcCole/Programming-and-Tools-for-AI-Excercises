"""Extension. Letting the computer pick the right decoding.

Run the tests:

    python -m doctest W01/E13_caesar_crack.py

No output means every test passed.

QUESTION: crack fails on the short message below. Why? What would you
need in order to fix it? Write your answer in the comment at the bottom.
"""

# Given: the cipher from the lecture. You do not need to change it.
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar(s, k):
    """Shift every letter of s forward by k places. Leave other characters alone."""
    shifted = ALPHABET[k % 26:] + ALPHABET[:k % 26]
    out = []
    for c in s:
        if c in ALPHABET:
            out.append(shifted[ALPHABET.index(c)])
        else:
            out.append(c)
    return "".join(out)


def all_shifts(s):
    """Given: every possible decoding, as (k, plaintext) tuples."""
    return [(k, caesar(s, -k)) for k in range(26)]


def english_score(text):
    """Score how English-looking text is: count the commonest English letters.

    The six commonest letters in English are e, t, a, o, i, n. Count how
    many characters of text are one of those. Upper case counts too.

    >>> english_score("hello there")
    5
    >>> english_score("xyz")
    0
    >>> english_score("attack at dawn")
    8
    """
    score = 0
    for letter in text:
        #finding out if the letter in text is in etaoin at thsi stage of the for loop
        if letter.lower() in 'etaoin':
            score+=1#adding to score if the letter is present
    return score


def crack(s):
    """Return the decoding of s that scores highest. No human required.

    >>> crack("wkh txlfn eurzq ira")
    'the quick brown fox'
    >>> crack("dvvk dv rk kyv sizuxv rk urne")
    'meet me at the bridge at dawn'
    >>> crack("ymj wfns ns xufns kfqqx rfnsqd ts ymj uqfns")
    'the rain in spain falls mainly on the plain'

    But it is only a guess, and on a short message it guesses wrong:

    >>> crack("khoor zruog")
    'ebiil tloia'
    """
    allShiftedValues = all_shifts(s)#give every possible value of s shifted
    bestScore = -1#starting at -1 as to overwite the score on first iteration
    bestGuess = ''

    for valueNumberInShift, valueGuessInShift in allShiftedValues:
        current_score = english_score(valueGuessInShift)#scoring each valueGuessInShift in for loop
        #if the score below is better than the last then assign the values 
        if current_score > bestScore:
            bestScore = current_score
            bestGuess = valueGuessInShift

    return bestGuess
    


# Crack fails on Khoor zruog as the code requires letter frequency to be higher to allow
#the most common letters functionality to work.
