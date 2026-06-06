class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            if target - nums[i] in mapping and i != mapping[(target-nums[i])]:
                return sorted([i, mapping[(target-nums[i])]])
            mapping[nums[i]] = i

