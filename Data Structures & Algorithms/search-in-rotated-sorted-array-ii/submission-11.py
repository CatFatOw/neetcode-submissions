class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Array of nums: arr
        search if target is in the nums 


        EXAMPLE:  nums = [3,4,4,5,6,1,2,2], target = 1

        notice this we can view it as two parts 
        [3,4,4,5,6] and [1,2,2]
        in this case we can see that we can search for one in either the left or te thr right side :D 
        """

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            # Check if its valid 
            if nums[mid] == target:
                return True 
            
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            else:
                # Check which part of the arary it is in 
                # is in the first half 
                if nums[left] <= nums[mid]:
                    # check if to move left to right 
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid +1
                
                else:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False
                        
        