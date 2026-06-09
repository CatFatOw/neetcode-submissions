class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        k = len(result) - 1

        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                result[k] = nums[right] ** 2
                right -= 1
            else:
                result[k] = nums[left] ** 2
                left += 1
            k -= 1
        return result



        