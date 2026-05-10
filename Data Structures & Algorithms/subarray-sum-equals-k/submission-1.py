from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        mapping = defaultdict(int)
        ans = 0

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[len(prefix)-1])
        print(prefix)
        
        ans = 0
        mapping[0] = 1
        # prefix[right] - prefix[left] + nums[left] = k
        # mapping[prefix[left] - nums[left]] = prefix[right]-k
        for right in range(len(nums)):
            ans += mapping[prefix[right] - k]
            mapping[prefix[right]] += 1
        return ans


        
       