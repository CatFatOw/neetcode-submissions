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

    
        
        def dfs(root, max_node_val):
            if not root:
                return 0
            count = 0
            if root.val >= max_node_val:
                max_node_val = root.val
                count += 1 + dfs(root.left, max_node_val) + dfs(root.right, max_node_val)
            else:
                count += dfs(root.left, max_node_val) + dfs(root.right, max_node_val)
            return count 
        return dfs(root, root.val) 
            
        