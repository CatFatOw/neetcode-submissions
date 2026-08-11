class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        total = 0
        left = 0
        count = 1

        for right in range(len(nums)):
            count *= nums[right]

            while count >= k and left < right:
                count /= nums[left]
                left += 1
            
            if count < k:
                total += right-left+1
        return total

        