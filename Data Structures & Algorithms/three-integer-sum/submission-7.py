from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mapping = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i != j:
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    val = -(nums[i] + nums[j])
                    mapping[val].append([i, j])
        
        result = set()
        for k in range(len(nums)):
            if nums[k] in mapping:
                for i, j in mapping[nums[k]]:
                    if i != k and j != k:
                        temp = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(temp)
        return [list(x) for x in result]


        