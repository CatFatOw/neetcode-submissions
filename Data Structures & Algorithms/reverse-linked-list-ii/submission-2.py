# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next= head
        # identify node before left and node after right 
        counter = 0
        node_before_left = None
        node_after_right = None
        ptr = dummy
        while ptr:
            if counter == left-1:
                node_before_left = ptr
            if counter == right + 1:
                node_after_right = ptr
                break
            counter += 1
            ptr = ptr.next


        # Basically standard reverse linked list logic

        # Find the starting left node
        curr_ptr = node_before_left.next
        prev = node_after_right
        

        while curr_ptr and curr_ptr != node_after_right:
            temp = curr_ptr.next 
            curr_ptr.next = prev
            prev = curr_ptr
            curr_ptr = temp
        # once done reversing our curr_ptr should be on the ending right node, which we need to reconnect with our inital node
        node_before_left.next = prev
        return dummy.next





