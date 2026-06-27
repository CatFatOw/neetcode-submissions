# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(root, state):
            # Top down approach
            if not root:
                return 0
            if (root, state) in memo:
                return memo[(root, state)]
            
            # ntkaen
            if state == 1:
                best = dp(root.left, 0) + dp(root.right, 0)
            else:
                rob = root.val + dp(root.left, 1) + dp(root.right, 1)
                skip = dp(root.left, 0) + dp(root.right, 0)

                best = max(rob, skip)
            
            memo[(root, state)] = best 
            return best 
        
        return dp(root, 0)
        