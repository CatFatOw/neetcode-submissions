class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    # found triplet
                    temp = [nums[i], nums[left], nums[right]]
                    result.append(temp)
                    while nums[left] in temp and left < right:
                        left += 1
                    while nums[right] in temp and left < right:
                        right -= 1

                if val > 0:
                    right -= 1
                
                if  val < 0:
                    left += 1
        return result