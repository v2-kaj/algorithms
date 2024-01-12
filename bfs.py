def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        current_vertex = queue[0]
        queue = queue[1:] #remove the first element from the original list
        if current_vertex not in visited:
            print(current_vertex, end=' ')
            visited.add(current_vertex)
            queue.extend(neighbor for neighbor in graph[current_vertex] if neighbor not in visited)
    print() # just to move the cursor to the next line after printing the nodes

# Example usage
g3 = {
    'a': ['b', 'c'],
    'b': ['d', 'e', 'f'],
    'c': ['h'],
    'd': [],
    'e': [],
    'f': ['g'],
    'g': [],
    'h': ['g']
}

start_vertex = 'a'
print("BFS starting from vertex", start_vertex)
bfs(g3, start_vertex) #abcdfe