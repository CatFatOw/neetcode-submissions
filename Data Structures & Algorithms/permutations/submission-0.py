class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        def backtrack(i):
            if i == len(nums):
                result.append(temp.copy())
                return 
            
            for j in range(len(nums)):
                if nums[j] in temp:
                    continue
                temp.append(nums[j])
                backtrack(i+1)
                temp.pop()
        backtrack(0)
        return result

        