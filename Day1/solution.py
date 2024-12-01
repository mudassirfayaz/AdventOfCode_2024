def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

# Example input


with open("adventofCode2024/input.txt") as f:
    lines = [[int(i) for i in l.split()] for l in f]
# Part 1
l1, l2 = [list(sorted(x)) for x in zip(*lines)]
print(sum(abs(a-b) for a, b in zip(l1, l2)))

# left_list = [3, 4, 2, 1, 3, 3]
# right_list = [4, 3, 5, 3, 9, 3]

# Call the function
total_distance = calculate_total_distance(l1, l2)
print("Total Distance:", total_distance)
