def dfs(i, j, visited, grid, n, m):
    visited[i][j] = 1
    # Check 4 directions: up, right, down, left
    for r, c in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nRow = i + r
        nCol = j + c
        if (
            0 <= nRow < n and
            0 <= nCol < m and
            grid[nRow][nCol] == "1" and
            visited[nRow][nCol] == 0
        ):
            dfs(nRow, nCol, visited, grid, n, m)

def numIslands(grid):
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])
    visited = [[0] * m for _ in range(n)]  # Create visited grid

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and visited[i][j] == 0:
                dfs(i, j, visited, grid, n, m)
                count += 1  # Found a new island
    return count

# Example usage
grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"]
]

print(numIslands(grid))  # Output: 3


















