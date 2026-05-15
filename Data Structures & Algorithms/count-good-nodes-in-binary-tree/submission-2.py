# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_node = root.val

        def dfs(root, max_node):
            if not root:
                return 0
            
            if root.val >= max_node:
                left = dfs(root.left, max(max_node, root.val))
                right =  dfs(root.right, max(max_node, root.val))
                return 1 + right + left
            else:
                left = dfs(root.left, max(max_node, root.val))
                right = dfs(root.right, max(max_node, root.val))
            return left + right 
        return dfs(root, max_node) 

