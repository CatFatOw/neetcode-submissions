class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Pivot index: index where sum of all numbers strictly to the left is equal to the sum of 
        numbers strictly to the right
        else 
        -1
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[len(prefix)-1])
        
        for idx in range(len(prefix)):
            left_sum = prefix[idx] - prefix[0] + nums[0]
            right_sum = prefix[len(prefix)-1] - prefix[idx] + nums[idx]
            if left_sum == right_sum:
                return idx 
        return -1

        
        

        