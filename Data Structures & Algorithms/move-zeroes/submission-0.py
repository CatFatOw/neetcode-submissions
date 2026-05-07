class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_arr = list()
        length = len(nums)
        copied = nums.copy()
        for i in range(length):
            if copied[i] == 0:
                nums.remove(copied[i])
                zero_arr.append(0)
        nums.extend(zero_arr)