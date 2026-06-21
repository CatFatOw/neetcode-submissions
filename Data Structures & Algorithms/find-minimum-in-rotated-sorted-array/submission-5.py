class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2

            # This means mid is on the first sorted section while right is 
            # on the second sorted section
            # We know the second sorted section is always less in value so
            if nums[mid] > nums[right] and nums[left] > nums[right]:
                left = mid + 1
            # This means both mid and right are in the same section
            # nums[mid] could already be the minimum so
            elif nums[mid] <= nums[right]:
                if nums[mid-1] > nums[mid]:
                    return nums[mid] 
                else:
                    right = mid-1
        return nums[mid]


                
            
            
                
        