from heapq import heappush, heappop
from collections import namedtuple

Node = namedtuple('Node', ['score', 'y', 'x', 'dir', 'c'])

# Process the input to include only valid numeric characters
with open("./Day17/input.txt", "r") as f:
    pInput = [
        [int(char) for char in line.strip() if char.isdigit()] 
        for line in f
    ]

width, height = len(pInput[0]), len(pInput)

def isOOB(y, x):
    """Check if the given (y, x) is out of bounds of the grid."""
    return y < 0 or y >= height or x < 0 or x >= width

alldirs = ((0, 1, '>'), (1, 0, 'V'), (0, -1, '<'), (-1, 0, 'A'))
opposite = {a: b for a, b in zip('<>AV', '><VA')}

MIN, MAX = (1, 3)
MIN, MAX = (4, 10)

def expand(node):
    """Generate neighboring nodes for the UCS algorithm."""
    for dy, dx, dir in alldirs:
        if opposite[node.dir] == dir:
            continue
        if dir != node.dir and node.c < MIN:
            continue
        new_y = node.y + dy
        new_x = node.x + dx
        if isOOB(new_y, new_x):
            continue
        if dir == node.dir:
            if node.c < MAX:
                yield Node(node.score + pInput[new_y][new_x], new_y, new_x, dir, node.c + 1)
        else:
            yield Node(node.score + pInput[new_y][new_x], new_y, new_x, dir, 1)

def ucs():
    """Uniform Cost Search to find the optimal path."""
    closed = set()
    open = []
    heappush(open, Node(0, 0, 0, '>', 0))
    heappush(open, Node(0, 0, 0, 'V', 0))

    while open:
        node = heappop(open)
        if node.y == height - 1 and node.x == width - 1 and node.c >= MIN:
            return node.score
        if node[1:] in closed:
            continue
        closed.add(node[1:])
        for s in expand(node):
            heappush(open, s)

    return -1

print(ucs())
