def read_input(filename):
    with open(filename) as fin:
        lines = fin.read().strip().split("\n")
    positions = []
    velocities = []
    for line in lines:
        a, b = line.split(" ")
        positions.append(list(map(int, a.split("=")[1].split(","))))
        velocities.append(tuple(map(int, b.split("=")[1].split(","))))
        positions[-1] = [positions[-1][1], positions[-1][0]]
        velocities[-1] = [velocities[-1][1], velocities[-1][0]]
    return positions, velocities

def update_positions(positions, velocities, n, m):
    for i in range(len(positions)):
        positions[i][0] = (positions[i][0] + velocities[i][0] + n) % n
        positions[i][1] = (positions[i][1] + velocities[i][1] + m) % m

def detect_christmas_tree(grid, n, m):
    # Define the Christmas tree pattern
    tree_pattern = [
        "   #   ",
        "  ###  ",
        " ##### ",
        "#######",
        "   #   "
    ]
    tree_height = len(tree_pattern)
    tree_width = len(tree_pattern[0])

    for i in range(n - tree_height + 1):
        for j in range(m - tree_width + 1):
            match = True
            for ti in range(tree_height):
                for tj in range(tree_width):
                    if tree_pattern[ti][tj] == '#' and grid[i + ti][j + tj] != '#':
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

def part2(filename):
    n = 103
    m = 101
    positions, velocities = read_input(filename)
    step = 0

    while True:
        # Initialize the grid
        grid = [['.' for _ in range(m)] for _ in range(n)]
        for x, y in positions:
            grid[x][y] = '#'

        # Check for the Christmas tree pattern
        if detect_christmas_tree(grid, n, m):
            print(f"Christmas tree pattern detected at step {step}.")
            break

        # Update positions for the next step
        update_positions(positions, velocities, n, m)
        step += 1

# Run Part 2
part2("./Day14/input.txt")
