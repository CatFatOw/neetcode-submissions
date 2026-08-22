# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root, rob):
            if not root:
                return 0
            if (root, rob) in memo:
                return memo[(root, rob)]
            
            if rob:
                best = root.val + dp(root.left, rob=False) + dp(root.right, rob=False)
            else:
                best =  max(dp(root.left, rob=True), dp(root.left, False)) + max(dp(root.right, rob=True), dp(root.right, False))

            
            memo[(root,rob)]= best 
            return best 
        return max(dp(root, False), dp(root, True))
        