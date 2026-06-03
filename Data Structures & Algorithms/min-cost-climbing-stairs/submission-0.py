class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            # Base case 
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            # recurrance relation
            best = min(cost[i] + dp(i-1), cost[i] + dp(i-2))
            memo[i] = best
            return best 
        return min(dp(len(cost)-1), dp(len(cost)-2))

        