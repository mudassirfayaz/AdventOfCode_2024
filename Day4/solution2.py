def count_xmas(input_file):
    # Read input
    with open(input_file, 'r') as f:
        grid = [line.strip() for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])

    # Directions for the X-shape:
    # (row_offset, col_offset) -> Direction for top-left to bottom-right, and top-right to bottom-left diagonals
    directions = [(-1, -1), (-1, 1)]

    def check_xmas(r, c):
        # Check if we can form an X-MAS starting at (r, c)
        # We need at least 3 rows and columns to form an X
        if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
            return 0
        
        count = 0
        for dr, dc in directions:
            # Check diagonal direction (dr, dc)
            # We need to check both forward "MAS" and backward "SAM"
            # 1st diagonal: grid[r-1][c-1] -> M, grid[r][c] -> A, grid[r+1][c+1] -> S
            # 2nd diagonal: grid[r-1][c+1] -> M, grid[r][c] -> A, grid[r+1][c-1] -> S
            if (grid[r - 1][c - 1] == 'M' and grid[r][c] == 'A' and grid[r + 1][c + 1] == 'S') or \
               (grid[r - 1][c + 1] == 'M' and grid[r][c] == 'A' and grid[r + 1][c - 1] == 'S'):
                count += 1
        return count

    # Iterate over all possible starting points in the grid
    total_xmas = 0
    for r in range(1, rows - 1):  # Start from row 1 to rows-1 to avoid out-of-bounds
        for c in range(1, cols - 1):  # Start from column 1 to cols-1 to avoid out-of-bounds
            total_xmas += check_xmas(r, c)

    return total_xmas

# Example usage:
input_file = "./Day4/input.txt"
print("Total X-MAS count:", count_xmas(input_file))
