# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Do DFS starting at the root of one of the trees and compare it with the other"
        """

        def dfs(root_p, root_q):
            if not root_p and not root_q:
                return True 
            
            if (root_p and not root_q) or (not root_p and root_q):
                return False 

            if root_p.val != root_q.val:
                return False 
            
            left = dfs(root_p.left, root_q.left)
            right = dfs(root_p.right, root_q.right)
            return left and right
        return dfs(p, q)
        