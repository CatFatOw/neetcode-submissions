"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = defaultdict(int)
        curr = head 
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next 
        
        # We do this to store the val -> node relation
        dummy = Node(0)
        curr = dummy
        ptr = head
        while ptr:
            node = old_to_new[ptr]
            # update the new node :D
            node.random = old_to_new.get(ptr.random)
            node.next = old_to_new.get(ptr.next)
            
            curr.next = node 
            ptr = ptr.next
            curr = curr.next
        return dummy.next





