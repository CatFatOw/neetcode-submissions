# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            robbed = root.val
            if root.right:
                robbed += dp(root.right.left)
                robbed += dp(root.right.right)
            if root.left:
                robbed += dp(root.left.right)
                robbed += dp(root.left.left)

            skip = dp(root.left) + dp(root.right)
            best = max(robbed, skip)
            memo[root] = best
            return best
        return dp(root)


        