"""Extension. What "fewest roads" costs you, in minutes.

Run the tests:

    python -m doctest W06/E06_route.py

No output means every test passed.

`E01_river.py` has both searches in it already: `bfs_graph`, which minimises
the number of edges, and `dijkstra`, which minimises the total weight. Run
both on `ROADS` and the difference between them is a number of minutes.
"""

from E01_river import ROADS, bfs_graph, dijkstra, road_time, roads_from


def time_lost(start, goal):
    """How many minutes the fewest-roads route costs you over the quickest.

    Zero where the two searches happen to agree, which is most of this map.

    >>> time_lost("Galway", "Roundstone")
    35
    >>> time_lost("Cong", "Carna")
    35
    >>> time_lost("Galway", "Clifden")
    0
    >>> time_lost("Galway", "Galway")
    0
    """
    #this function compares BFS and dijkstra
    #BFS ignores edge weights and treats every road segment as having an equal cost of 1
    bfs_route = bfs_graph(ROADS, start, goal)
    #find the lowest total weight of driving times from start to goal using dijkstras algorithm
    quickest_cost, _ = dijkstra(roads_from, start, goal)
    return road_time(bfs_route) - quickest_cost


def quickest_times(start):
    """The quickest time from `start` to every town on the map, as a dict.

    >>> times = quickest_times("Galway")
    >>> times["Roundstone"]
    70
    >>> times["Clifden"]
    72
    >>> times["Galway"]
    0
    >>> len(times) == len(ROADS)
    True

    >>> quickest_times("Clifden")["Galway"]
    72
    """
    return
