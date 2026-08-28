# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

  
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        tree1 = inorder(root1)
        tree2 = inorder(root2)

        # we now have two sorted list, les see if (target - x ) is in the set of other list 
        for num in tree1:
            if (target-num) in set(tree2):
                return True 
        return False

        