# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 

        saved_prev, curr = dummy, head 
        for _ in range(left-1):
            saved_prev = saved_prev.next
            curr = curr.next 

        prev = None 
        start = curr
        for _ in range(right-left+1):
            # list traversal
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp

        start.next = curr 
        saved_prev.next = prev
        return dummy.next

        
        



        



