# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Main logic: 
        Reverse the Linked list 
        if the reversal == original we say true otherwise false :) 
        """
        og_stack = []
        reversed_stack = []

        ptr = head 
        while ptr:
            og_stack.append(ptr.val)
            ptr = ptr.next 
        
        # lets reverse it now 
        curr = head 
        prev= None 
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        
        ptr = prev 
        while ptr:
            reversed_stack.append(ptr.val)
            ptr = ptr.next 
        return og_stack == reversed_stack