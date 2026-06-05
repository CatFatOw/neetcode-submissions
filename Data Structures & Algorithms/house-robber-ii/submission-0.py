class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dp(i, robbed_first):
            if i >= len(nums):
                return 0 
            if (i, robbed_first) in memo:
                return memo[(i, robbed_first)]
            
            # If we robbed first
            if robbed_first and i == len(nums) - 1:
                best = 0
            else:
                best = max(nums[i] + dp(i+2, robbed_first), dp(i+1, robbed_first))
            memo[(i, robbed_first)] = best 
            return best 
        return max(dp(0, True), dp(1, False))

        