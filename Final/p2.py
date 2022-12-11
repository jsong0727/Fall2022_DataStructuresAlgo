class Solution:
    def numOfIsland(self, grid):
        if not grid: return 0

        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for (dr, dc) in directions:
                dfs(row+dr, col+dc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
        return islands

# time: O(m*n)
# space: O(m*n)

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid3 = [[]]
a = Solution()
print(a.numOfIsland(grid))
print(a.numOfIsland(grid2))
print(a.numOfIsland(grid3))
