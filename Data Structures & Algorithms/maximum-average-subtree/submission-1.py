# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return 0

        max_avg = 0

        def dfs(root):
            nonlocal max_avg
            if not root:
                return 0,0
            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total = left_sum + right_sum + root.val 
            count = left_count + right_count + 1
            max_avg = max(max_avg, total/count)
            return total, count
        dfs(root)
        return max_avg
        