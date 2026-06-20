# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next:
            return 0
        # Logic to get the length of the linked list
        stack = []
        curr = head 
        counter = 0
        while curr:
            counter += 1
            curr = curr.next 

        # half it
        mid = counter//2
        curr = head
        counter = 0 
        # Logic to get the stack
        while curr:
            if counter < mid:
                stack.append(curr.val)
            curr = curr.next
            counter += 1
        # Logic to get twin sum
        ans = 0
        counter = 0
        curr = head
        while curr:
            if counter >= mid:
                ans = max(ans, stack.pop()+curr.val)
                
            curr = curr.next
            counter += 1
        return ans

        