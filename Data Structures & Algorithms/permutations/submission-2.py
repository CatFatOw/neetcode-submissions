class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        return all possible permutations: order does matter

        BASE CASE:
        if i == len(nums)


        RECURRANCE CASE:
        use a for loop nad check if the resultant is not in the answer
        """

        result = []
        def backtrack(i, arr):
            if i == len(nums):
                result.append(arr.copy())
                return None 
            
          
            for idx in range(0, len(nums)):
                if nums[idx] in arr:
                    continue
                
                arr.append(nums[idx])
                backtrack(i+1, arr)
                arr.pop(-1)
            
        backtrack(0, [])
        return result
        