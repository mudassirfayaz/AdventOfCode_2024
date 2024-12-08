from operator import add, mul
from itertools import product

# Read input from the file
with open("./Day7/input.txt") as f:
    lines = [x.strip().split(": ") for x in f]

# Function to evaluate an expression with given operators
def evaluate_expression(ops, numbers):
    result = numbers[0]
    for num, op in zip(numbers[1:], ops):
        result = op(result, num)
    return result

# Part 1
allowed_ops_part1 = [add, mul]
res_part1 = 0
for chunk1, chunk2 in lines:
    expected_result = int(chunk1)
    args = [int(c) for c in chunk2.split()]

    # Generate all possible combinations of allowed operators for the given numbers
    for ops in product(allowed_ops_part1, repeat=len(args)-1):
        curr_res = evaluate_expression(ops, args)
        if curr_res == expected_result:
            res_part1 += expected_result
            break

# Part 2
allowed_ops_part2 = [add, mul, lambda a, b: int(f"{a}{b}")]  # Include concatenation (||)
res_part2 = 0
for chunk1, chunk2 in lines:
    expected_result = int(chunk1)
    args = [int(c) for c in chunk2.split()]

    # Generate all possible combinations of allowed operators for the given numbers
    for ops in product(allowed_ops_part2, repeat=len(args)-1):
        curr_res = evaluate_expression(ops, args)
        if curr_res == expected_result:
            res_part2 += expected_result
            break

# Print the results for both parts
print(f"Answer for Part 1: {res_part1}")
print(f"Answer for Part 2: {res_part2}")
