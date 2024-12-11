with open("./Day10/input.txt") as f:
    lines = [[int(i) for i in x.strip()] for x in f]

bounds = len(lines)

def follow_trail(x, y, curr, visited, is_part1):
    if curr == 9:
        if not is_part1: return 1
        if (x, y) not in visited:
            visited.add((x, y))
            return 1
        return 0
    
    res = 0
    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= nx < bounds and 0 <= ny < bounds:
            n = lines[ny][nx]
            if n == curr + 1:
                res += follow_trail(nx, ny, n, visited, is_part1)
    return res

for is_part1 in [True, False]:
    res = 0
    for y, line in enumerate(lines):
        for x, i in enumerate(line):
            if i == 0:
                res += follow_trail(x, y, i, set(), is_part1)
    print(res)