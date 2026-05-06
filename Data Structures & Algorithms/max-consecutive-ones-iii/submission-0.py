class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0
        left = 0
        flipped_ones = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                curr += 1
            else:
                flipped_ones += 1
                curr += 1
            while flipped_ones > k:
                if nums[left] == 1:
                    curr -=1
                else:
                    flipped_ones -= 1
                    curr -= 1
                left += 1
            ans = max(ans, curr)
        return ans
        