class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [self.nums[0]] * len(self.nums)
        for i in range(1, len(self.nums)):
            self.prefix[i] = self.nums[i] + self.prefix[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 >= 0:
            return self.prefix[right] - self.prefix[left-1]
        else:
            return self.prefix[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)