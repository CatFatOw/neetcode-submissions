class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in memo:
                return memo[i]
            best = dp(i-1) + dp(i-2)
            memo[i] = best 
            return best 
        return dp(n)

        