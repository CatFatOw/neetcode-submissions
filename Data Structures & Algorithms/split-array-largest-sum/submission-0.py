class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def ok(mid, nums, k):
            total = 0
            counter = 0
            for i in range(len(nums)):
                if total +nums[i] > mid:
                    counter += 1
                    total = nums[i]
                else:
                    total += nums[i]
            return counter >= k

        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right)//2
            if ok(mid, nums, k):
                left = mid + 1
            else:
                right = mid-1
        return left
        