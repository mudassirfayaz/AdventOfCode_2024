from tqdm import tqdm

# Read and parse input
with open("./Day15/input.txt") as fin:
    parts = fin.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]
    steps = parts[1].replace("\n", "")

n = len(grid)

dirs = {
    "<": [0, -1],
    "v": [1, 0],
    ">": [0, 1],
    "^": [-1, 0]
}

# Initialize positions and structures
boxes, walls = [], []
for i in range(n):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            ci, cj = i, j
        elif grid[i][j] == "O":
            boxes.append([i, j])
        elif grid[i][j] == "#":
            walls.append([i, j])

# Helper function to check if a position is within bounds
def in_grid(i, j):
    return 0 <= i < n and 0 <= j < len(grid[0])

# Function to move in the specified direction
def move(direction):
    global ci, cj

    newi, newj = ci + direction[0], cj + direction[1]
    if not in_grid(newi, newj) or [newi, newj] in walls:
        return

    stack, seen = [], set()

    if [newi, newj] in boxes:
        stack.append([newi, newj])

    # Determine if movement is possible
    can_move = True
    while stack:
        topi, topj = stack.pop()
        ni, nj = topi + direction[0], topj + direction[1]

        if not in_grid(ni, nj) or [ni, nj] in walls:
            can_move = False
            break

        if (topi, topj) in seen:
            continue
        seen.add((topi, topj))

        if [ni, nj] in boxes:
            stack.append([ni, nj])

    if not can_move:
        return

    # Move boxes
    for i, box in enumerate(boxes):
        if tuple(box) in seen:
            boxes[i][0] += direction[0]
            boxes[i][1] += direction[1]

    # Move player
    ci, cj = newi, newj

# Simulate steps
for step in tqdm(steps):
    move(dirs[step])

# Calculate result
ans = sum(i * 100 + j for i, j in boxes)
print(ans)
