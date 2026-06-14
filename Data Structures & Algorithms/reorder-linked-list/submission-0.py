# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next 
        
        curr = head
        for i in range(len(stack)//2):
            node = stack.pop()
            temp = curr.next

            curr.next = node
            node.next = temp
            curr = temp
        # Sever the cycle
        curr.next = None 

       

        