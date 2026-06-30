# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        leaves = []
        left = []
        right = []

        def is_leaf(node):
            return node and not node.left and not node.right

        def get_leaves(node):
            if not node:
                return
            if is_leaf(node):
                leaves.append(node.val)
                return
            get_leaves(node.left)
            get_leaves(node.right)

        def get_left(root):
            if is_leaf(root) or not root:
                return None 
            left.append(root.val)

            if root.left:
                get_left(root.left)
            else:
                get_left(root.right)

        def get_right(root):
            if not root or is_leaf(root):
                return None 
            right.append(root.val)
            if root.right:
                get_right(root.right)
            else:
                get_right(root.left)
            

        



        get_leaves(root)
        get_left(root.left)
        get_right(root.right)

        return [root.val] + left + leaves + list(reversed(right))

        
    
        