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
        mapping = {}
        start = head 
        while start:
            mapping[start] = Node(start.val, start.next, start.random)
            start = start.next 
        
        ptr = head 
        while ptr:
            node = mapping[ptr]
            node.next = mapping.get(ptr.next)
            node.random = mapping.get(ptr.random)
            ptr = ptr.next
        if head not in mapping:
            return None 
        return mapping[head]
        