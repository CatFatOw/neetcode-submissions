# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, prev, counter, max_counter):
            if not root:
                return counter
            if (root.val - prev.val) == 1:
                counter += 1
            left = dfs(root.left, root, counter,max(max_counter, counter))
            right = dfs(root.right, root, counter, max(max_counter, counter))
            return max(left, right)
        return dfs(root, root,0, 0) + 1
        