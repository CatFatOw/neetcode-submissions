class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0
        left = 0
        flipped = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                curr_ones += 1
            if nums[right] == 0:
                flipped += 1
                curr_ones += 1
            
            while flipped > 1:
                if nums[left] == 0:
                    flipped -= 1
                curr_ones -= 1
                left += 1
            max_ones = max(max_ones, curr_ones)
        return max_ones
