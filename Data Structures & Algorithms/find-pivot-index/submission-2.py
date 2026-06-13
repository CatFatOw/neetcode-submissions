class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        
        
        #print(prefix)
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 0
            right = prefix[-1] - prefix[i]
            if left == right:
                return i
        return -1
