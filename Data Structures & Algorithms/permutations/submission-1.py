class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        visited = set()

        def backtrack(arr):
            # Base case is len(arr) == nums
            if len(arr) == len(nums):
                result.append(arr.copy())
                return 
            
            # If not the arr
            for num in nums:
                # If seen before 
                if num in visited:
                    continue
                arr.append(num)
                visited.add(num)
                backtrack(arr)
                arr.pop()
                visited.remove(num)
        backtrack([])
        return result 
                
        