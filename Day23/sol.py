from collections import defaultdict

def find_triangles_with_t(connections):
    # Build an adjacency list from the input connections
    graph = defaultdict(set)
    for conn in connections:
        a, b = conn.split('-')
        graph[a].add(b)
        graph[b].add(a)
    
    triangles = set()
    
    # Find all triangles
    for node in graph:
        for neighbor1 in graph[node]:
            for neighbor2 in graph[node]:
                if neighbor1 < neighbor2 and neighbor2 in graph[neighbor1]:
                    triangle = tuple(sorted([node, neighbor1, neighbor2]))
                    triangles.add(triangle)
    
    # Filter triangles where at least one computer name starts with 't'
    triangles_with_t = [triangle for triangle in triangles if any(comp.startswith('t') for comp in triangle)]
    return len(triangles_with_t), triangles_with_t

# Read input from file
with open("./Day23/input.txt", "r") as file:
    connections = [line.strip() for line in file if line.strip()]

# Solve the problem
triangle_count, triangles_with_t = find_triangles_with_t(connections)

# Output the results
print(f"Number of triangles containing a computer starting with 't': {triangle_count}")
