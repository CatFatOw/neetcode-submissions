class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            # Skip adj duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            left = i + 1
            right = len(nums)-1

            while left < right:
                if i != left and i != right:
                    val = nums[left] + nums[right] + nums[i]
                    if val == 0:
                        temp = [nums[left], nums[right], nums[i]]
                        result.append(temp)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1

                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    elif val > 0:
                        right -= 1
                    else:
                        left += 1
        return result
        