import re

def sum_mul_results(corrupted_memory):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all valid mul matches
    matches = re.findall(pattern, corrupted_memory)
    
    # Compute the sum of products
    total = sum(int(x) * int(y) for x, y in matches)
    
    return total

# Example corrupted memory input
# corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("./Day3/input.txt", "r") as f:
    corrupted_memory = f.read()
# Call the function and print the result
result = sum_mul_results(corrupted_memory)
print("Total sum of valid mul results:", result)
