# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the nth node first 
        slow = head 
        fast = head 
        for _ in range(n):
            fast = fast.next 
        while fast:
            slow = slow.next 
            fast = fast.next 
        nth_node = slow 
        
        dummy = ListNode()
        dummy.next = head 
        ptr1 = dummy
        ptr2 = dummy.next 
        while ptr2:
            if ptr2 == nth_node:
                ptr1.next = ptr2.next 
                break
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next 
        return dummy.next