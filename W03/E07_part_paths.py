"""Extension. Carrying information down the recursion.

Run the tests:

    python -m doctest W03/E07_part_paths.py

No output means every test passed.
"""

# Given: the bicycle from the lecture. You do not need to change it.
bicycle = {
    "name": "bicycle", "qty": 1, "children": [
        {"name": "wheel", "qty": 2, "children": [
            {"name": "rim",   "qty": 1,  "material": "aluminium", "mass": 380},
            {"name": "spoke", "qty": 32, "material": "steel",     "mass": 5},
            {"name": "hub",   "qty": 1,  "material": "steel",     "mass": 200},
            {"name": "tyre",  "qty": 1,  "material": "rubber",    "mass": 320},
        ]},
        {"name": "frame",     "qty": 1, "material": "steel",     "mass": 2200},
        {"name": "handlebar", "qty": 1, "material": "aluminium", "mass": 300},
        {"name": "saddle",    "qty": 1, "material": "plastic",   "mass": 260},
        {"name": "chain",     "qty": 1, "material": "steel",     "mass": 300},
    ],
}


def part_paths(node, prefix=""):
    """Return the full path of every part you buy, deepest name last.

    Everything so far has passed answers back up the tree. This passes
    something down: each call builds the path of the node it is looking at
    and hands it to its children, exactly as depth was handed down in the
    lecture's debugging version of unit_mass.

    prefix is where the caller is; do not set it yourself when you call
    part_paths from outside.

    >>> for path in part_paths(bicycle):
    ...     print(path)
    bicycle/wheel/rim
    bicycle/wheel/spoke
    bicycle/wheel/hub
    bicycle/wheel/tyre
    bicycle/frame
    bicycle/handlebar
    bicycle/saddle
    bicycle/chain

    The path of a part depends on where you started, not on where it lives:

    >>> part_paths(bicycle["children"][0])
    ['wheel/rim', 'wheel/spoke', 'wheel/hub', 'wheel/tyre']
    >>> part_paths(bicycle["children"][1])
    ['frame']
    """
    #the following line takes the following expression 
    #<value_if_true> if <condition> else <value_if_false>
    #so the current path is the prefix followed by the node[name] but id the
    #prefix exists it is just node[name]
    current_path = f"{prefix}/{node['name']}" if prefix else node["name"]

    #the following assigns the current path to the return statement
    #if there are no children of the node
    if "children" not in node:
        return [current_path]
    #pass the accumulated current_path downward to all descendants,
    #then flatten the resulting lists using extend().
    paths = []
    for child in node["children"]:
        paths.extend(part_paths(child, current_path))
    return paths


def find_part(node, path):
    """Return the part at the given path, or raise KeyError if there is none.

    >>> find_part(bicycle, "bicycle/wheel/hub")["mass"]
    200
    >>> find_part(bicycle, "bicycle/frame")["material"]
    'steel'
    >>> find_part(bicycle, "bicycle")["name"]
    'bicycle'
    >>> find_part(bicycle, "bicycle/wheel/axle")
    Traceback (most recent call last):
        ...
    KeyError: 'bicycle/wheel/axle'
    """
    #if the path = node[name] equates to true return the node
    if path == node["name"]:
        return node


    prefix = node["name"] + "/"
    if path.startswith(prefix) and "children" in node:
        #strip the current node name and separator to pass only the sub-path downward.
        remaining_path = path[len(prefix):]
        #traverse direct children to search for the remaining path segment.
        for child in node["children"]:
            try:
                #if a child branch finds the node, return it.
                return find_part(child, remaining_path)
            except KeyError:
                #if the child did not have it continue to the next child
                pass
                
    raise KeyError(path)
