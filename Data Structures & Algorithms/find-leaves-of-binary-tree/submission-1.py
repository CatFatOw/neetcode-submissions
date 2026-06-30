# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = defaultdict(list)
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            height = 1 + max(left, right)
            mapping[height].append(root.val)
            return height
        dfs(root)
        return [y for x, y in sorted(mapping.items())]


        