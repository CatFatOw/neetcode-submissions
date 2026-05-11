from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        we use a prefix sum + hashmap appraoch 
        prefix[j] - prefix[i] = k
        prefix[i] = prefix[j] - k
        """

        ans = 0
        mapping = defaultdict(int)
        # Seen prefix sum of 0 once 
        mapping[0] = 1
        prefix = 0

        for num in nums:
            prefix += num
            ans += mapping[prefix-k]
            mapping[prefix] += 1
        return ans

        