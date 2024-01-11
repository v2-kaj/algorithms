def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            print(current_vertex, end=' ')
            visited.add(current_vertex)
            stack.extend(neighbor for neighbor in graph[current_vertex] if neighbor not in visited)
    print() # just to move the cursor to the next line after printing the nodes

# Example usage
g3 = {
    'a': ['b'],
    'b': ['c', 'd' ],
    'c': ['f'],
    'd': ['e'],
    'e': [],
    'f': [],
}

start_vertex = 'a'
print("DFS starting from vertex", start_vertex)
dfs(g3, start_vertex) #abdecf

