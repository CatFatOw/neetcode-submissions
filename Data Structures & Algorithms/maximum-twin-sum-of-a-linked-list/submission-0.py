# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = list()
        counter = 0
        limit = 0
        
        ptr = head
        # find the length
        while ptr:
            limit += 1
            ptr = ptr.next

        ans = 0
        while head:
            if counter >= limit//2:
                if stack:
                    val = stack.pop().val
                    ans = max(ans, val + head.val)
            else:
                stack.append(head)
                counter += 1
            head  = head.next
        return ans
