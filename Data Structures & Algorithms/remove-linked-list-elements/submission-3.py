# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        ptr = dummy
        ptr.next = head 

        while ptr and ptr.next:
            while ptr and ptr.next and ptr.next.val == val:
                ptr.next = ptr.next.next
                
            ptr = ptr.next 
        
        ptr = dummy
        while ptr and ptr.next and ptr.next == val:
            ptr.next = ptr.next.next
        return dummy.next