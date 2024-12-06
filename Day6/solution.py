from itertools import cycle

def traverse_path(pos_x, pos_y, obstacles, bound):
    visited = set()
    visited.add((pos_x, pos_y))

    dirs = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    dir_x, dir_y = next(dirs)
    
    cache = set()
    cache.add((pos_x, pos_y, dir_x, dir_y))

    while True:
        new_x, new_y = pos_x + dir_x, pos_y + dir_y

        # If we hit an obstacle -> turn
        if (new_x, new_y) in obstacles:
            dir_x, dir_y = next(dirs)

        # If we hit the border -> done
        elif new_x < 0 or new_x >= bound or new_y < 0 or new_y >= bound:
            return False, visited

        # Else -> continue walking
        else:
            pos_x, pos_y = new_x, new_y
            visited.add((pos_x, pos_y))

            # If we visit the same position in the same direction -> loop detected
            c = (pos_x, pos_y, dir_x, dir_y)
            if c in cache:
                return True, visited
            else:
                cache.add((pos_x, pos_y, dir_x, dir_y))


with open("./Day6/input.txt") as f:
    lines = [list(x.strip()) for x in f]
bound = len(lines)

obstacles = set()
pos_x, pos_y = 0, 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#": obstacles.add((x,y))
        elif c == "^": pos_x, pos_y = x, y

# Part 1
_, visited = traverse_path(pos_x, pos_y, obstacles, bound)
print(len(visited))

# Part 2
# Check of position of new obstacle only on the traversed path of the guard
candidates = visited - {(pos_x, pos_y)}

print(sum(traverse_path(pos_x, pos_y, obstacles | {cand}, bound)[0] for cand in candidates))