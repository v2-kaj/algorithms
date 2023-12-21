
"""
Example 1

a---b---c
|   |
d---e

"""
undirected = {
    'a': ['b', 'd',],
    'b': ['a', 'c', 'e',],
    'c': ['b',],
    'd': ['a', 'e',],
    'e': ['b','d',],
}



