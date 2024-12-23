from heapq import heappush, heappop
from collections import defaultdict

# Read input
with open("./Day16/input.txt") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)
start, end = None, None
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)

dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Dijkstra's Algorithm - Part 1 and Part 2
q = [(0, 0, *start, 0, *start)]  # (cost, direction, i, j, previous_direction, previous_i, previous_j)
cost = {}
dept = defaultdict(list)
seen = set()
seen_pos = set()
while q:
    top = heappop(q)
    c, d, i, j, pd, pi, pj = top

    if (d, i, j) in cost:
        if cost[(d, i, j)] == c:
            dept[(d, i, j)].append((pd, pi, pj))
        continue

    if (i, j) not in seen_pos:
        dept[(d, i, j)].append((pd, pi, pj))
        seen_pos.add((i, j))

    cost[(d, i, j)] = c

    if grid[i][j] == "#":
        continue

    if grid[i][j] == "E":
        end_dir = d
        print("Part 1 Answer:", c)
        break

    ii, jj = i + dd[d][0], j + dd[d][1]

    for nbr in [
        (c + 1, d, ii, jj, d, i, j),
        (c + 1000, (d + 1) % 4, i, j, d, i, j),
        (c + 1000, (d + 3) % 4, i, j, d, i, j),
    ]:
        heappush(q, nbr)

# Part 2: Trace back through dependencies
stack = [(end_dir, *end)]
seen.clear()
seen_pos.clear()
while stack:
    top = stack.pop()
    if top in seen:
        continue
    seen.add(top)
    seen_pos.add(top[1:])

    for nbr in dept[top]:
        stack.append(nbr)

print("Part 2 Answer:", len(seen_pos))
