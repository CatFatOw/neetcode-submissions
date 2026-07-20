class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = []

        def backtrack(i, arr):
            if i == len(nums):
                results.append(arr.copy())
                return 
            

            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()

            backtrack(i+1, arr)
        
        backtrack(0, [])
        return results

        