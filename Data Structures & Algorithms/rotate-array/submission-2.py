class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            dummy = [0] * k
            dummy.extend(nums)
            # modify the orignal 
            nums[:] = dummy

            ptr = 0
            end = len(nums)-1
            for _ in range(k-1):
                ptr += 1

            
            while ptr >= 0 and end >= 0:
                nums[ptr] = nums[end]
                end -= 1
                ptr -= 1
            
            # Clean it up
            for _ in range(k):
                nums.pop(-1)
            
        

        