class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
    
        # Now the slow/fast pointer is at the intersection point, we need to find the 
        # start of the cycle

        ptr1 = nums[0]
        while ptr1 != slow:
            ptr1 = nums[ptr1]
            slow = nums[slow]
        return ptr1
        