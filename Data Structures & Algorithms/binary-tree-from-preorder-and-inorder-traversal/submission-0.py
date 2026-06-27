# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def tree_build(preorder, inorder):
            if not preorder or not inorder:
                return None 
            
            root = TreeNode(preorder[0])
            # get the index
            mid = inorder.index(preorder[0])
            # everything left is [:mid], right is [mid+1:]
            root.left = tree_build(preorder[1:mid+1], inorder[:mid])
            root.right = tree_build(preorder[mid+1:], inorder[mid+1:])
            return root
        return tree_build(preorder, inorder)
        