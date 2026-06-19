# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get the middle value :D
        length = 0
        curr = head 
        while curr:
            length += 1
            curr = curr.next 
        mid = length // 2

        # Push the stack values :D 
        stack = []
        counter = 0
        curr = head
        for _ in range(length):
            if counter >= mid:
                stack.append(curr)
            counter += 1
            curr = curr.next 
        
        # Pass2: find the value :D
        ans = 0
        curr = head
        for _ in range(mid):
            twin_sum = curr.val + stack.pop().val
            ans = max(ans, twin_sum)
            curr = curr.next
        return ans


        