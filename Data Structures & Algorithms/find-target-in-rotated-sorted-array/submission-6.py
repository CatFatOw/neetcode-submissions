class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] > nums[right]:
                if nums[right] == target:
                    return right
                else:
                    right -= 1
            
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid 
                
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        