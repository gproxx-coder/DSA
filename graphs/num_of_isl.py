# https://leetcode.com/problems/number-of-islands/

def number_of_islands(grid):
    def dfs(grid, x, y, rows, cols):
        if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != '1':
            return

        if grid[x][y] == '1':
            grid[x][y] = '2'

        dfs(grid, x, y + 1, rows, cols)  # Right
        dfs(grid, x + 1, y, rows, cols)  # Down
        dfs(grid, x, y - 1, rows, cols)  # Left
        dfs(grid, x - 1, y, rows, cols)  # Top

    no_of_isl = 0
    rows, cols = len(grid), len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                dfs(grid, i, j, rows, cols)
                no_of_isl += 1
    print("NOI:", no_of_isl)


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    number_of_islands(grid)
