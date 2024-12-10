with open("./Day9/input.txt") as f:
    disk_code = [int(i) for i in "".join(x.strip() for x in f)]

d = {}
frees = []

counter = 0
for i, r in enumerate(disk_code):
    start, end = counter, counter + r
    if i % 2 == 0:
        d[i//2] = (start, end)
    elif r > 0:
        frees.append((start, end))
    counter += r

# Observation:
#   We never move files from left to right.
#   Therefore, when moving a file, I do not care about the gap that file leaves at its source location.
#   Therefore, I do not track these gaps.

# Two pointers: 
#   One that is tracking the file index and moves from the highest file index to 0.
#   One that is searching for the next free gap and repeatedly runs from 0 to the start of the current file.

idx_ptr = max(d.keys())

while idx_ptr >= 0:
    file_start, file_end = d[idx_ptr]
    file_len = file_end - file_start

    free_ptr = 0
    while free_ptr < len(frees):
        gap_start, gap_end = frees[free_ptr]
        if gap_start >= file_start:
            break

        gap_len = gap_end - gap_start
        if file_len <= gap_len:
            frees.pop(free_ptr)

            new_file_start, new_file_end = gap_start, gap_start + file_len
            new_gap_start, new_gap_end = new_file_end, gap_end

            d[idx_ptr] = (new_file_start, new_file_end)
            if new_gap_start != new_gap_end:
                frees.insert(free_ptr, (new_gap_start, new_gap_end))
            break
        else:
            free_ptr += 1

    idx_ptr -= 1

res = 0
for k, (start, end) in d.items():
    res += sum(k*i for i in range(start, end))
print(res)