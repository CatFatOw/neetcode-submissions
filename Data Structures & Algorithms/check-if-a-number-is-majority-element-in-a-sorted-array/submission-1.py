class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """
        nums: increasing order 
        and target

        GOAL: check if target is majority element  (appears more than nums.length / 2 times in the array)

        EXAMPLE:
        [2,4,5,5,5,5,6,6], target = 5
        then
        we can binary search all the way to the left 

        so if 

        say left is at 4 then we can say 

        APPORACH:
        binary serach the first occurance the target
        binary search the last occurance the target
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                right = mid - 1
            else:
                left = mid + 1
        
        left2 = 0
        right2 = len(nums)-1
        while left2 <= right2:
            mid = (left2+right2)//2
            if nums[mid] == target:
                left2 = mid + 1
            else:
                right2 = mid-1

        return right2-left + 1 > len(nums)/2
        

            
