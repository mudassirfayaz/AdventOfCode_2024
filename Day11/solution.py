from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import defaultdict
import sys

sys.setrecursionlimit(2**30)

def part1():
    with open("./Day11/input.txt") as fin:
        nums = list(map(int, fin.read().strip().split()))

    def blink(arr):
        res = []
        for x in arr:
            if x == 0:
                res.append(1)
            elif len(str(x)) % 2 == 0:
                l = len(str(x))
                res += [int(str(x)[:l // 2]), int(str(x)[l // 2:])]
            else:
                res += [x * 2024]
        return res

    plot = []
    for i in tqdm(range(25)):
        nums = blink(nums)
        plot.append(len(nums))

    plt.plot(plot)
    plt.show()

    return len(nums)

def part2():
    with open("./Day11/input.txt") as fin:
        raw_nums = list(map(int, fin.read().strip().split()))

    nums = defaultdict(int)
    for x in raw_nums:
        nums[x] += 1

    def blink(nums: dict):
        new_nums = defaultdict(int)
        for x in nums:
            l = len(str(x))
            if x == 0:
                new_nums[1] += nums[0]
            elif l % 2 == 0:
                new_nums[int(str(x)[:l // 2])] += nums[x]
                new_nums[int(str(x)[l // 2:])] += nums[x]
            else:
                new_nums[x * 2024] += nums[x]
        return new_nums

    for i in range(75):
        nums = blink(nums)

    ans = sum(nums.values())
    return ans

# Print results
print("Part 1 result:", part1())
print("Part 2 result:", part2())
