# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        diff = float("inf")

        def dfs(root, target, diff):
            nonlocal ans
            if not root:
                return 0
            
            node_diff = abs(target-root.val)
            if node_diff < diff:
                diff = node_diff 
                ans = root.val 
            
            dfs(root.left, target, diff)
            dfs(root.right, target, diff)
        dfs(root, target, diff)
        return ans