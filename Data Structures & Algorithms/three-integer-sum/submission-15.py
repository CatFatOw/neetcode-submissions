class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                ans = [nums[i], nums[left], nums[right]]
                if nums[i] + nums[left] + nums[right] == 0 and ans not in result:
                    result.append(ans)
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result
                    
        