class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        result = []

        def backtrack(start, total):
            if total == target:
                result.append(temp.copy())
            
            for i in range(start, len(nums)):
                if sum(temp) > target:
                    return 
                else:
                    temp.append(nums[i])
                    backtrack(i, total + nums[i])
                    temp.pop()

        backtrack(0, 0)
        return result