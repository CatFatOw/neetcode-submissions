from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        # do a two sum apporach :D 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    val = nums[i] + nums[j] + nums[left] + nums[right]
                    if val == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in result:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif val > target:
                        right -= 1
                    else:
                        left += 1
        return result




                    
