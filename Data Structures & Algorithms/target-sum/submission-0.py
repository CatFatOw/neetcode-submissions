class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx, curr):
            if idx == len(nums):
                return 1 if curr == target else 0
            if (idx, curr) in memo:
                return memo[(idx, curr)]
            
            best = dp(idx+1, curr + nums[idx]) + dp(idx+1, curr-nums[idx])
            memo[(idx, curr)] = best 
            return best 
        
        return dp(0,0)