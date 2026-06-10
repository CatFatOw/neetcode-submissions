class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            # do i+1 to avoid duplicates
            for j in range(i+1, len(nums)):
                # Make sure no duplicates 
                if j > i+1 and nums[j] == nums[j-1] or i > 0 and nums[i] == nums[i-1]:
                    continue 
                left = j+1
                right = len(nums)-1

                # Don't want them to be equal
                while left < right:
                    if i != left and i != right and j != left and j != right:
                        val = nums[i] + nums[j] + nums[left] + nums[right]
                        if val == target:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                            right -= 1
                            left += 1

                            # skip the duplicates as next value may also produce same solution
                            while left < right and nums[left] == nums[left-1]:
                                left += 1
                            while left < right and nums[right] == nums[right+1]:
                                right -= 1
                        elif val > target:
                            right -= 1
                        else:
                            left += 1
        return result
            