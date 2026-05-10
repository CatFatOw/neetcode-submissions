from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        mapping = defaultdict(int)

        for num in nums:
            mapping[num] += 1
        ans = -1
        for num, freq in mapping.items():
            if freq == 1:
                ans = max(ans, num)
        return ans
        