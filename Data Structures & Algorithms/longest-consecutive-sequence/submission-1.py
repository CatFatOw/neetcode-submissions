from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        target_nums = []
        unique_nums = set(nums)
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
            if num-1 not in unique_nums:
                target_nums.append(num)
        
        best = 1
        
        for num in target_nums:
            temp = 1
            while num + 1 in mapping:
                temp += 1
                num += 1
            best = max(best, temp)
        return best
        
        