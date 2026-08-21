class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        length n
        
        the array was roated leftwares between 1, len(nums) timesd 

        given the rotated sorted array and target, return true if the target is in the array else false 


        APPORACH:
        notice that we hqave two soroted regions

        1. binary serach mid 
        2. if left <= target < mid we in the left half. if mid <= target < right its in the other half
        3. then based on this we move and manipulate the pointers ;D 
        """
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2

           

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue 

            # case 1 in the left sorted region
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

        