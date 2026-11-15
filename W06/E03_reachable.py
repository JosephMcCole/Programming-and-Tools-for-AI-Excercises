"""Composition. Search with no goal: where could we possibly get to? SOLUTION.

Run the tests:

    python -m doctest W06/E03_reachable.py

No output means every test passed.

`bfs` stops as soon as it finds the goal. Take the goal away and let it run to
exhaustion, and what you have explored is the whole connected part of the
graph. That is how you find out how big a state space really is.
"""

from collections import deque
#First in first out deque functionality here, order of 1 capability
from E01_river import ROADS, START, successors


def reachable(successors, start):
    """Every state reachable from `start`, as a set. `start` itself counts.

    Breadth-first search with the goal test removed: keep a frontier and a
    visited set, and stop when the frontier runs dry.

    The river has sixteen states on paper and ten that are safe, and every
    safe one can actually be reached:

    >>> len(reachable(successors, START))
    10

    A dict is not a successor function, but a `lambda` turns it into one:

    >>> len(reachable(lambda town: ROADS[town], "Galway"))
    12
    >>> sorted(reachable(lambda n: {"a": "b", "b": "a", "c": ""}[n], "c"))
    ['c']
    """

    #Breadth first search
    #visited is a set containing the starting state
    #order of 1 which does require states be hashable
    visited = {start}
    #states are explored outward layer by layer in the frontier variable
    frontier = deque([start])
    #while there are non explored states in the queue which is denoted here by the frontier variable
    while frontier:
        #assigning node to the left sides state that has been waiting longest in the queue
        node = frontier.popleft()
        #for each neighbour a single move from node 
        for neighbour in successors(node):
            #if the neighbour is not in visited add to visited and for the purposes of the loop
            #add to frontier at the end so it can be explored later
            if neighbour not in visited:
                visited.add(neighbour)
                frontier.append(neighbour)
    #returning the visited nodes
    return visited


def connected(successors, a, b):
    """Is there any route at all from `a` to `b`?

    >>> connected(successors, "LLLL", "RRRR")
    True

    "LLRR" is the wolf and the goat left alone together. It is a state you can
    write down, and there is no way to reach it:

    >>> connected(successors, "LLLL", "LLRR")
    False
    """
    #returns boolean answer if there is a route from a to b
    return b in reachable(successors, a)