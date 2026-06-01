from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        

        def backtrack(i):
            if i == len(nums):
                result.append(temp.copy())
                return 
            
            for num in mapping:
                if mapping[num] > 0:
                    mapping[num] -= 1
                    temp.append(num)
                    backtrack(i+1)
                    temp.pop(-1)
                    mapping[num] += 1
        backtrack(0)
        return result
        