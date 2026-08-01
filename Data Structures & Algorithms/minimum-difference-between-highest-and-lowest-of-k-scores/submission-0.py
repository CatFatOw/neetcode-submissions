class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # After sorting the minimum is left and max is nums[right]
        nums.sort()
        min_difference = float("inf")
        
        for right in range(k):
            ...
        min_difference = min(min_difference, nums[right]-nums[0])

        for right in range(k, len(nums)):
            min_difference = min(min_difference, nums[right]-nums[right-k+1])
        return min_difference



