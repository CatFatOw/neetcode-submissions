# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if not root:
                return None 
            min_val = min(p.val, q.val)
            max_val = max(p.val, q.val)
            if min_val <= root.val <= max_val:
                return root
            
            if root.val < min_val:
                return dfs(root.right, p, q)
            else:
                return dfs(root.left, p, q)
        return dfs(root, p, q)
        