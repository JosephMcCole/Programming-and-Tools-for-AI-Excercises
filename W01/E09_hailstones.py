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

    sequence=[n]#storing the first number entered into the return value sequence
    while n > 1:
        if n%2 == 0:#if the n modulous 2 is 0 so ture
            n = n//2# divide n by 2, // forces interger division
        else:
            n = 3*n+1#else do 3 times n plus 1
        sequence.append(n) #add n to hailstone sequence
    return sequence





def longest_hailstone(limit):
    """Return (n, length) for the longest hailstone sequence with n < limit.

    >>> longest_hailstone(10)
    (9, 20)
    >>> longest_hailstone(100)
    (97, 119)
    >>> longest_hailstone(1000)
    (871, 179)
    """

    # largest_n = 0
    # longest_sequence = 0
    # count = []
    # for n in range(0,limit):
    #     longest_sequence = len(hailstones(n))+1
    #     count.append(longest_sequence)
    #     print(max(count))
    # for j in range(1,max(count)):

    best_n,best_l = 1,1#double assignment of variables on one line, both to 1
    for n in range(1,limit):
        #generating the longest sequence for n and measuring its length
        longest_sequence = len(hailstones(n))
        #on this step in the for loop the longest sequence if better than best_l
        #is then assigned to best_l 
        if longest_sequence > best_l:
        #if the best_l and best_n here are the longest in the sequence, then
        #update the best n and best l to the winning numbers
            best_n,best_l = n,longest_sequence
    return(best_n,best_l)#returning here as a tuple

   

# y = longest_hailstone(10)
# print(y)
