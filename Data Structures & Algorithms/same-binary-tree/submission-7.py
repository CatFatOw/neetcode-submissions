# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True 
            if (not p and q) or (p and not q):
                return False
            
            if p.val != q.val:
                return False 
            
            # if (p.left and  not q.left) or (not p.left and q.left):
            #     return False 
            # if (p.right and not p.right) or (not p.right and q.right):
            #     return False 
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left and right
        return dfs(p, q)

