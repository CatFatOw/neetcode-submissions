# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        root: BST tree
        val: vaslue to insert


        APPORACH: do BST/BINARY SERACH STYLE, etc. if at the current root noe more compare it if its < or > etc and then insert :D 
        """
        def insert(root, val):
            if not root:
                return TreeNode(val)
           
            
            if root.val < val:
                root.right = insert(root.right, val)
            
            if root.val > val:
                root.left = insert(root.left, val)
            return root 
        return insert(root, val)
            

        