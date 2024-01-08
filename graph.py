
"""
Example 1
undirected graph
a---b---c
|   |
d---e

"""
example1_undirected = {
    'a': ['b', 'd',],
    'b': ['a', 'c', 'e',],
    'c': ['b',],
    'd': ['a', 'e',],
    'e': ['b','d',],
}


"""
Example 2
undirected graph
A to 1 weight 3
A to 2 weight 2
B to 1 weight 3
B to 2 weight 3
"""
example2_undirected = {
        'A': {'1': 3, '2': 2},
        'B': {'1': 3, '2': 3},
        '1': {'A': 3, 'B': 3},
        '2': {'A': 2, 'B': 3},
        }
# to access the weight of A to 2 which is 3
a1_weight = example2_undirected['A']['1'] 

# to access the weight of 2 to B which is 3
twob = example2_undirected['2']['B'] 

