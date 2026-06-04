class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dp(row, col):
            if row < 0 or col < 0:
                return float("inf")
            if row == 0 and col == 0:
                return grid[0][0]
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            best = grid[row][col] + min(dp(row-1, col), dp(row, col-1))
            memo[(row, col)] = best 
            return best 
        return dp(len(grid)-1, len(grid[0])-1)
        