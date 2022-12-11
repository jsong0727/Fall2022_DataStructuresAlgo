class Solution:
    def numOfPath(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            paths[0][0] = 1
        else:
            paths[0][0] = 0
        if paths[0][0] == 0:
            return 0
        # first row
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                paths[0][i] = paths[0][i-1]
        # first column:
        for i in range(1, m):
            if obstacleGrid[i][0] !=1:
                paths[i][0] = paths[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]

# time: O(m * n)
# space: O(m * n)

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
a = Solution()
print(a.numOfPath(obstacleGrid))