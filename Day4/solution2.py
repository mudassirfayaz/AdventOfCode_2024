import numpy as np

# Load and process the input
with open("./Day4/input.txt") as f:
    lines = [
        list(x.strip().replace("A", "3").replace("M", "2").replace("S", "4").replace("X", "1"))
        for x in f
    ]

img = np.array(lines).astype("uint8")

# Part 1

def find_part1(arr):
    # Check if the center element is "X"
    if arr[3, 3] == 1:
        pos = [
            tuple(arr[3, 4:7]),
            tuple(arr[3, 2::-1]),
            tuple(arr[4:7, 3]),
            tuple(arr[2::-1, 3]),
            tuple(arr[4:7, 4:7].diagonal()),
            tuple(arr[2::-1, 2::-1].diagonal()),
            tuple(arr[4:7, 2::-1].diagonal()),
            tuple(arr[2::-1, 4:7].diagonal()),
        ]
        return sum(p == (2, 3, 4) for p in pos)
    return 0

def apply_filter_part1(img):
    padded_img = np.pad(img, pad_width=3, mode="constant", constant_values=0)
    res = np.zeros_like(img, dtype=int)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded_img[i:i+7, j:j+7]
            res[i, j] = find_part1(region)

    return res

res_part1 = apply_filter_part1(img)
print(res_part1)
print(np.sum(res_part1))

# Part 2

def find_part2(arr):
    # Check if the center element is "A"
    if arr[1, 1] == 3:
        return any([
            arr[0, 0] == 2 and arr[0, 2] == 4 and arr[2, 0] == 2 and arr[2, 2] == 4,
            arr[0, 0] == 4 and arr[0, 2] == 2 and arr[2, 0] == 4 and arr[2, 2] == 2,
            arr[0, 0] == 2 and arr[0, 2] == 2 and arr[2, 0] == 4 and arr[2, 2] == 4,
            arr[0, 0] == 4 and arr[0, 2] == 4 and arr[2, 0] == 2 and arr[2, 2] == 2,
        ])
    return 0

def apply_filter_part2(img):
    padded_img = np.pad(img, pad_width=1, mode="constant", constant_values=0)
    res = np.zeros_like(img, dtype=int)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded_img[i:i+3, j:j+3]
            res[i, j] = find_part2(region)

    return res

res_part2 = apply_filter_part2(img)
print(res_part2)
print(np.sum(res_part2))