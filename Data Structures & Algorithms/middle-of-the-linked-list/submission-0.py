# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        ptr1 = dummy
        ptr2 = dummy

        
        while ptr2 and ptr2.next:
            ptr1 = ptr1.next 
            ptr2 = ptr2.next.next 
        
        if not ptr2:
            return ptr1
        elif ptr2 and not ptr2.next:
            return ptr1.next