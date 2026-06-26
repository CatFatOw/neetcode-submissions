# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(root, subRoot):
            if not root and not subRoot:
                return True 
            if not root or not subRoot:
                return False 
            
            if root.val != subRoot.val:
                return False 
            
            left = same_tree(root.left, subRoot.left)
            right = same_tree(root.right, subRoot.right)
            return left and right 
        
        def dfs(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False
            if same_tree(root, subRoot):
                return True
            
            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)
            return left or right
            
        return dfs(root, subRoot)

        