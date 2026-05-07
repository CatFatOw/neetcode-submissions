class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        sum_value = 0
        left = 0

        for right in range(len(nums)):
            sum_value += nums[right]

            while sum_value >= target:
                ans = min(ans, right-left+1)
                sum_value -= nums[left]
                left += 1
        if ans == float("inf"):
            return 0
        return ans
                
