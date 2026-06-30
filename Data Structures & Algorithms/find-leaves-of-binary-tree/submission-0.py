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
        def dfs_height(root):
            if not root:
                return -1
            left = dfs_height(root.left)
            right = dfs_height(root.right)
            return 1 + max(left, right)

        def dfs(root):
            if not root:
                return None 
            height = dfs_height(root)
            mapping[height].append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(mapping)
        return [y for x, y in sorted(mapping.items())]

        
        
        