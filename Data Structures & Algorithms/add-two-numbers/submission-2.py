# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy = ListNode()
        ptr = dummy

        while ptr1 or ptr2 or carry:
            
            v1 = ptr1.val if ptr1 else 0
            v2 = ptr2.val if ptr2 else 0

            val = v1 + v2 + carry
            digit = val % 10
            carry = val // 10
            ptr.next = ListNode(digit)

            # Populate the two pointers
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
            ptr = ptr.next

        while carry != 0:
            ptr.next = ListNode(carry%10)
            ptr = ptr.next
            carry = carry//10

        ptr.next = None
        return dummy.next

            


