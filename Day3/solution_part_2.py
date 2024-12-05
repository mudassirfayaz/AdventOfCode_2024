import re

# Read the input
with open("./Day3/input.txt", "r") as f:
    corrupted_memory = f.read()

# Regular expressions
mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")  # Matches valid mul(X,Y)
do_pattern = re.compile(r"do\(\)")  # Matches do()
dont_pattern = re.compile(r"don't\(\)")  # Matches don't()

# Initialize state
is_enabled = True
total = 0

# Process the memory character by character
i = 0
while i < len(corrupted_memory):
    # Check for do()
    if corrupted_memory[i:i + 4] == "do()":
        is_enabled = True
        i += 4
    # Check for don't()
    elif corrupted_memory[i:i + 7] == "don't()":
        is_enabled = False
        i += 7
    # Check for mul(X,Y)
    elif match := mul_pattern.match(corrupted_memory, i):
        if is_enabled:
            x, y = map(int, match.groups())
            total += x * y
        i += match.end() - match.start()
    else:
        # Move to the next character if no match
        i += 1

# Output the result
print(f"The total sum of enabled multiplications is: {total}")
