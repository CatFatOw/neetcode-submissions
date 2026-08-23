# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        return true if height balanced

        height-balanced is if the left and right subtrees of every node differ by <= 1

        APPROACH:

        do DFS every time it a leaf node I compare it and constantlhy update the lefta nd right sections
        """
        balanced = True
        def dfs(root):
            nonlocal balanced
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right) > 1:
                balanced = False
            return 1 + max(left, right)
        dfs(root)
        return balanced

        
        