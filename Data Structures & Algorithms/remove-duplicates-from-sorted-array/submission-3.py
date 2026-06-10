class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        k = 0
        last= nums[-1]

        for i in range(1, len(nums)):
            # Since sorted the duplicates are adjacent
            # No duplicates
            if nums[i] != nums[i-1]:
                nums[ptr] = nums[i-1]
                ptr += 1
                k += 1
        nums[ptr] = nums[-1]
        return k + 1

                
                
            
            