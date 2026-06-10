from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mapping = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    val = -(nums[i] + nums[j])
                    mapping[val].append([i, j])
        
        result = []
        for k in range(len(nums)):
            if nums[k] in mapping:
                for i, j in mapping[nums[k]]:
                    if i != k and j != k:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        if not temp in result:
                            result.append(temp)
        return result


        