class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(row, col):
            if row < 0 or col < 0:
                return 0

            if row == 0 and col == 0:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            total = dp(row-1, col) + dp(row, col-1)
            memo[(row, col)] = total
            return total
        return dp(m-1, n-1)
        