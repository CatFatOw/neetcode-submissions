class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            best = 1
            for idx in range(i, len(nums)):
                if nums[idx] > nums[i]:
                    best = max(1 + dp(idx), best)
            memo[i] = best 
            return best 
        
        result = 1
        for i in range(len(nums)):
            result = max(dp(i), result)
        return result
        