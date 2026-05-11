from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        good subarray: length >= 2 and sum of elements is multiple of k

        prefix[j] - prefix[i] = m * k
        so we can say 
        prefix[j] % k == prefix[i] % k 
        """
        prefix = 0
        mapping = defaultdict(int)
        mapping[0] = -1

        for i in range(len(nums)):
            prefix += nums[i]
            if prefix % k in mapping and i - mapping[prefix % k] >= 2:
                return True 
            if prefix % k not in mapping:
                mapping[prefix % k] = i
        return False