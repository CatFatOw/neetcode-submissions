class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        def dp(row, col):
            if row < 0 or col < 0:
                return 0

            if row == 0 and col == 0 and obstacleGrid[row][col] == 0:
                return 1
            elif row == 0 and col == 0 and obstacleGrid[row][col] == 1:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            
            if obstacleGrid[row][col] != 1:
                best = dp(row-1, col) + dp(row, col-1)
            else:
                best = 0
            memo[(row, col)] = best 
            return best 
        return dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        