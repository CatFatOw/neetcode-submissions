from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mapping = defaultdict(int)
        mapping[0] = 1
        ans = 0
        prefix = 0

        for num in nums:
            prefix += num
            # prefifx[j] - prefix[i] = goal 
            # prefix[i] = prefix[j] - goal

            ans += mapping[prefix - goal]
            mapping[prefix] += 1
        return ans
        