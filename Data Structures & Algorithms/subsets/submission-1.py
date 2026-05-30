class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = [] 

        def backtrack(i):
            if i == len(nums):
                result.append(temp.copy())
                return 

            # Skip
            backtrack(i+1)
            
            # take the one 
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
        backtrack(0)
        return result