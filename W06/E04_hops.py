"""Composition. How far is everywhere, in moves? SOLUTION.

Run the tests:

    python -m doctest W06/E04_hops.py

No output means every test passed.

One BFS answers "how far is the goal?" for every goal at once, because a
state is first reached along a shortest path to it. Keep the distance instead
of the predecessor and you get the whole table for the price of one search.

QUESTION: `hops_from` records a distance for a state the first time it sees
that state, and never changes it afterwards. Why is that safe here, and what
would go wrong on `ROADS` if the numbers we wanted were minutes rather than
roads? Write your answer in the comment at the bottom.
"""

from collections import deque

from E01_river import ROADS, START, successors


def hops_from(successors, start):
    """How many moves each reachable state is from `start`, as a dict.

    `start` itself is 0. Everything else is one more than the state it was
    first reached from.

    >>> hops_from(successors, START)["RRRR"]
    7
    >>> hops_from(successors, START)["RLRL"]
    1

    Four roads from Galway to Clifden, whichever way you go:

    >>> hops_from(lambda town: ROADS[town], "Galway")["Clifden"]
    4
    >>> hops_from(lambda n: {"a": "b", "b": "a"}[n], "a") == {"a": 0, "b": 1}
    True
    """
    #declaring distances as a dict
    distances = {start: 0}
    #starting frontier as a double ended queue
    frontier = deque([start])

    #loops until the queue is empty meaning every reachable state has been discovered
    while frontier:
        #removes and assigns frontiers oldest state to node, order of one
        node = frontier.popleft()
        #finds out how many moves to reach node from start
        current_dist = distances[node]
        for neighbour in successors(node):
            if neighbour not in distances:
                #records neighbour as visited and sets the distance to be one more than node
                distances[neighbour] = current_dist + 1
                frontier.append(neighbour)

    return distances


def farthest_hops(successors, start):
    """The distance to the state that is hardest to reach from `start`.

    >>> farthest_hops(successors, START)
    7
    >>> farthest_hops(lambda town: ROADS[town], "Galway")
    4
    """
    #returns the highest value in the returned values from the hops from function 
    return max(hops_from(successors, start).values())


#BFS arrives at the shortest path when it reachs a state and does not need to be updated later
#BFS if it used minutes these would be weights and BFS locks in the fewest roads or edges
#so a route with shorter time may have more roads but a route with fewer roads would be selected
