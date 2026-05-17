# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert_bst(root, val):
            if not root:
                return None 

            # Ending/where we insert :3
            if root and not root.left and not root.right:
                if root.val > val:
                    root.left = TreeNode(val)
                else:
                    root.right = TreeNode(val)
            elif root and root.left and not root.right:
                if root.val > val:
                    insert_bst(root.left, val)
                else:
                    root.right = TreeNode(val)
            elif root and root.right and not root.left:
                if root.val < val:
                    insert_bst(root.right, val)
                else:
                    root.left = TreeNode(val)
            else:
                if  root.val > val:
                    insert_bst(root.left, val)
                else:
                    insert_bst(root.right, val)
        insert_bst(root, val)
        return root


            
            

            
            