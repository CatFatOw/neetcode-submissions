# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, leaves):
            if not root:
                return None 
            if not root.left and not root.right:
                leaves.append(root.val)
                return None 
            
            root.left = dfs(root.left, leaves)
            root.right = dfs(root.right, leaves)
            return root 
        
        result = []
        while root:
            leaves = []
            root = dfs(root, leaves)
            result.append(leaves)
        return result