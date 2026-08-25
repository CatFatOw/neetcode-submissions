"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        """
        each node has reference to parent

        ok this is interesting

        1. start at p and q since we have reference to the parent we can "backward dfs traverse the tree"

        2. we stop at the first instance of ta shared node :D 

        make sure depth align

        """

        def depth(root, node, count):
            if not root:
                return 0
            
            if root == node:
                return count
            
            left = depth(root.left, node, count+1)
            right = depth(root.right, node, count+1)
            return max(left, right)
        


        depth_p = depth(root, p, 0)
        depth_q = depth(root, q, 0)
            
        def dfs(p, q):
            nonlocal depth_p
            nonlocal depth_q

            if not p and not q:
                return None 
            
            if p == q:
                return p
            
            if depth_p > depth_q:
                depth_p -= 1
                return dfs(p.parent, q)
            elif depth_p < depth_q:
                depth_q -= 1

                return dfs(p, q.parent)
            else:
                depth_p -=1
                depth_q -= 1
                return dfs(p.parent, q.parent)
           
        return dfs(p, q)

            
            