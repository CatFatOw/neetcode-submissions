class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid % 2 == 0:
                # Before the middle 
                if mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                    left = mid + 1
                # After the middle 
                elif mid-1 >= 0 and nums[mid] == nums[mid-1]:
                    right = mid - 1
                # the single element happened
                else:
                    return nums[mid]
            # Odd and before mid
            elif mid-1 >= 0 and nums[mid] ==nums[mid-1]:
                left = mid + 1
            #odd and after mid 
            elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
                right = mid - 1

            