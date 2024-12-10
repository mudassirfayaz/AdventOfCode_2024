from collections import defaultdict
from itertools import combinations

with open("./Day8/input.txt") as f:
    lines = [x.strip() for x in f]

bounds = len(lines)

d = defaultdict(list)
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            d[c].append((x, y))

antinodes1 = set()
antinodes2 = set()

for locations in d.values():
    for (xa, ya), (xb, yb) in combinations(locations, 2):
        dx, dy = xa - xb, ya - yb

        nx, ny = xa + dx, ya + dy
        mx, my = xb - dx, yb - dy
        if 0 <= nx < bounds and 0 <= ny < bounds: antinodes1.add((nx, ny))
        if 0 <= mx < bounds and 0 <= my < bounds: antinodes1.add((mx, my))

        for i in range(50):
            nx, ny = xa + i*dx, ya + i*dy
            mx, my = xb - i*dx, yb - i*dy
            if 0 <= nx < bounds and 0 <= ny < bounds: antinodes2.add((nx, ny))
            if 0 <= mx < bounds and 0 <= my < bounds: antinodes2.add((mx, my))

print(len(antinodes1))
print(len(antinodes2))