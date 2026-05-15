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

            if root == q or root == p:
                return root
           
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right:
                return root
                
            elif left and not right:
                return left 
            elif right and not left:
                return right
            
        return dfs(root, p, q)


            