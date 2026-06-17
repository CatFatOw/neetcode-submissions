# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        """We split it into two sections:
        1. Traverse the linked list, keep counter
        2. Intiatie, prev with ptr and reverse the section until counter == right-1
        3. connect the prev.next with the stop.next
        """
        dummy = ListNode()
        dummy.next = head
        pre_left = dummy
        left_ptr = head

        for _ in range(left-1):
            pre_left = pre_left.next
            left_ptr = left_ptr.next
        
        start = left_ptr
        prev = None
        for _ in range(right-left+1):
            temp = left_ptr.next 
            left_ptr.next = prev
            prev = left_ptr
            left_ptr = temp 

        
        # the position now should be a section that is reverse, but not connected and another section that is in its original format
        
        pre_left.next = prev
        start.next = left_ptr
            
        return dummy.next






        