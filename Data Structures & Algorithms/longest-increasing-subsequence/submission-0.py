class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            longest = 1
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    val = 1 + dp(j)
                    longest = max(longest, val)
                    memo[i] = longest

            return longest
        max_val = set()
        for i in range(len(nums)-1, -1, -1):
            max_val.add(dp(i))
        return max(max_val)


        