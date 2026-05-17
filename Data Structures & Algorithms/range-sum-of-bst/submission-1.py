# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def BST_traversal(root):
            if not root:
                return 0
            
            if root.val < low:
                result =  BST_traversal(root.right)
            elif root.val > high:
                result  = BST_traversal(root.left)
            else:
                result = root.val + BST_traversal(root.left) + BST_traversal(root.right)
            return result
        return BST_traversal(root)
