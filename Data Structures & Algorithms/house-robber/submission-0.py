class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            best = max(nums[i] + dp(i-2), dp(i-1))
            memo[i] = best 
            return best 
        return dp(len(nums)-1)
        