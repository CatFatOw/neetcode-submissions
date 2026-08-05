class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_length = 0
        left = 0
        window_total = 0

        for right in range(len(nums)):
            window_total += nums[right]
            operations = (nums[right] * (right-left+1)) - window_total
            
            while operations > k:
                window_total -= nums[left]
                left += 1
                operations = (nums[right] * (right-left+1)) -window_total
            
            max_length = max(max_length, right-left+1)
        return max_length
            