from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = defaultdict(int)
        mapping[0] = 1

        ans = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            ans += mapping[curr-k]
            mapping[curr] += 1
        return ans

        