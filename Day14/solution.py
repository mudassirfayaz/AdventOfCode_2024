n = 103
m = 101

with open("./Day14/input.txt") as fin:
    lines = fin.read().strip().split("\n")

p = []
v = []

for line in lines:
    a, b = line.split(" ")
    p.append(list(map(int, a.split("=")[1].split(","))))
    v.append(tuple(map(int, b.split("=")[1].split(","))))

    p[-1] = [p[-1][1], p[-1][0]]
    v[-1] = [v[-1][1], v[-1][0]]

N = len(p)

def update():
    for i in range(N):
        p[i][0] = (p[i][0] + v[i][0] + n) % n
        p[i][1] = (p[i][1] + v[i][1] + m) % m

def count_robots(i0, i1, j0, j1):
    return sum(1 for i in range(i0, i1) for j in range(j0, j1) for ii, jj in p if i == ii and j == jj)

def part1():
    for _ in range(100):
        update()

    q0 = count_robots(0, n // 2, 0, m // 2)
    q1 = count_robots(n // 2 + 1, n, 0, m // 2)
    q2 = count_robots(0, n // 2, m // 2 + 1, m)
    q3 = count_robots(n // 2 + 1, n, m // 2 + 1, m)

    return q0, q1, q2, q3, q0 * q1 * q2 * q3

def part2():
    seen = {}
    step = 0

    while True:
        picture = [["  "] * m for _ in range(n)]
        for i, j in p:
            picture[i][j] = "##"

        picture = "\n".join(["".join(line) for line in picture])
        if picture in seen:
            return seen[picture], step
        seen[picture] = step

        update()
        step += 1

# Results
q0, q1, q2, q3, product = part1()
print("Part 1:")
print(f"Quadrants: {q0}, {q1}, {q2}, {q3}")
print(f"Product: {product}")

print("\nPart 2:")
start, end = part2()
print(f"Saw the repeated picture at step {start}, stopping at step {end}.")
