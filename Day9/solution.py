with open("./Day9/input.txt") as f:
    disk_map = list("".join(x.strip() for x in f))

expanded = []
for i, r in enumerate(disk_map):
    if i % 2 == 0:
        for k in range(int(r)):
            expanded.append(f"{i // 2}")
    else:
        for k in range(int(r)):
            expanded.append(".")

free_ptr = 0
end_ptr = len(expanded) - 1

while free_ptr < end_ptr:
    while expanded[free_ptr] != ".":
        free_ptr += 1
    while expanded[end_ptr] == ".":
        end_ptr -= 1

    expanded[free_ptr] = expanded[end_ptr]
    expanded[end_ptr] = "."
    
    free_ptr += 1
    end_ptr -= 1

s = [e for e in expanded if e != "."]
res = sum(i * int(k) for i, k in enumerate(s))
print(res)