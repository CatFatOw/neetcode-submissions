# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        # Slow should now be at the middle :D
        # Start the reversal process 
        prev = None 
        curr = slow  

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp 
        ptr1 = prev
        print(ptr1.val)

        # Ok that section is now reversed!
        ptr2 = head 
        ans = 0
        while ptr1 and ptr2:

            val = ptr1.val + ptr2.val
            ans = max(ans, val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ans




        