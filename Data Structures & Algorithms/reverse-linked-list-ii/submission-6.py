# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head 
        b4_left = dummy
        left_ptr = head 
        right_ptr = head

        # Accumulate the left pointer
        for _ in range(left-1):
            left_ptr = left_ptr.next
            b4_left = b4_left.next 
        
        # Accumulate the right pointer
        for _ in range(right):
            right_ptr = right_ptr.next 
            
        after_right = None 
        if right_ptr:
            after_right = right_ptr.next
        

        # Now lets reverse :D 
        prev = None 
        start = left_ptr
        curr = left_ptr 
        for _ in range(right-left+1):
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
        
        # its reversed the new head is prev
        b4_left.next = prev
        start.next = curr
        return dummy.next

        
        
        