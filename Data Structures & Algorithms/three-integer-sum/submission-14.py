class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()        
        result = []
        

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            left = k + 1
            right = len(nums)-1

            while left < right:
                if nums[k] + nums[left] + nums[right] == 0:
                    result.append([nums[k], nums[left], nums[right]])
                
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left <=right and nums[right] == nums[right+1]:
                        right -=1
                
                elif nums[k] + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    left += 1
        return result