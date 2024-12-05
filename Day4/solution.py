def read_input(file_path):
    # Read the grid from the input file
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_word(grid, word, row, col, dr, dc):
    # Check if the word fits starting at (row, col) in direction (dr, dc)
    for i in range(len(word)):
        r = row + dr * i
        c = col + dc * i
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != word[i]:
            return False
    return True

def count_xmas(grid):
    word = "XMAS"
    count = 0
    # Directions to search for: (dr, dc) represents row and column increments
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # vertical and horizontal
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonals
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for dr, dc in directions:
                if check_word(grid, word, r, c, dr, dc):
                    count += 1
    return count

def main():
    input_file = "./Day4/input.txt"
    grid = read_input(input_file)
    result = count_xmas(grid)
    print("The word 'XMAS' appears", result, "times.")

if __name__ == "__main__":
    main()
