from collections import defaultdict

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        # Found a maximal clique
        cliques.append(R)
        return
    for v in list(P):
        bron_kerbosch(R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]), graph, cliques)
        P.remove(v)
        X.add(v)

def find_largest_clique(connections):
    # Build the adjacency list
    graph = defaultdict(set)
    for conn in connections:
        a, b = conn.split('-')
        graph[a].add(b)
        graph[b].add(a)

    # Find all maximal cliques
    cliques = []
    nodes = set(graph.keys())
    bron_kerbosch(set(), nodes, set(), graph, cliques)

    # Find the largest clique
    max_clique = max(cliques, key=len)

    # Sort the nodes alphabetically for the password
    password = ','.join(sorted(max_clique))
    return password

# Read input from file
with open("./Day23/input.txt", "r") as file:
    connections = [line.strip() for line in file if line.strip()]

# Solve the problem
password = find_largest_clique(connections)

# Output the results
print(f"The password to get into the LAN party is: {password}")
