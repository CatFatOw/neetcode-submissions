# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        prev = dummy
        ptr = dummy.next 
        while ptr:
            if ptr.val == val:
                while ptr and ptr.val == val:
                    ptr = ptr.next
                    
                prev.next = ptr
        
            else:
                ptr = ptr.next 
                prev = prev.next 
        return dummy.next