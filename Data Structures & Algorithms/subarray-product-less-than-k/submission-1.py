class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        counter = 0
        left = 0
        total = 1

        for right in range(len(nums)):
            total *= nums[right]
            while total >= k and left < len(nums):
                total /= nums[left]
                left += 1
            if right - left + 1 >= 0:
                counter += right - left + 1
        return counter

        