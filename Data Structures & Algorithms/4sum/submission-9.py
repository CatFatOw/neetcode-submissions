class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                left = b + 1 
                right = len(nums)- 1 

                while left < right:
                    ans = [nums[a], nums[b], nums[left], nums[right]]
                    if nums[a] + nums[b] + nums[left] + nums[right] == target and ans not in result:
                        result.append(ans)
                        left += 1
                        right -= 1

                    elif nums[a] + nums[b] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        left += 1
                     

        return result



        