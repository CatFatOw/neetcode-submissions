class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums)):
            if i-1 >= 0:
                prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            if i+1 < len(nums):
                suffix[i] = suffix[i+1] * nums[i+1]
        
        result = []
        for i in range(len(prefix)):
            val = prefix[i] * suffix[i]
            result.append(val)
        return result
        