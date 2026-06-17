class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        print(slow, fast)
        # now move them until they are equal 
        node = nums[0]
        while node != fast:
            node = nums[node]
            fast = nums[fast]
        return node