from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dp(i):
            if i >= len(nums):
                return 1
            if i in memo:
                return memo[i]

            max_len = 1
            for idx in range(i, len(nums)):
                if nums[idx] > nums[i]:
                    max_len = max(max_len, 1+dp(idx))

            memo[i] = max_len
            return max_len

        longest = 0
        for i in range(len(nums)):
            result = dp(i)
            print(result)
            longest = max(result, longest)
        return longest