from collections import defaultdict

with open("./Day5/input.txt") as f:
    constraints, updates = [x.split() for x in f.read().split("\n\n")]

d = defaultdict(list)
for c in constraints:
    a, b = c.split("|")
    d[a].append(b)


part1 = 0
part2 = 0

def repair_update(ud):
    new_ud = []
    for u in ud:
        counter = len(new_ud)
        while u in d and any(k in new_ud[:counter] for k in d[u]):
            counter -= 1
        new_ud.insert(counter, u)

    return int(new_ud[len(new_ud) // 2])
    
for update in updates:
    ud = update.split(",")
    
    for i, u in enumerate(ud):
        if u in d and any(k in ud[:i] for k in d[u]):
            part2 += repair_update(ud)
            break
    else:
        part1 += int(ud[len(ud) // 2])

print(part1)
print(part2)