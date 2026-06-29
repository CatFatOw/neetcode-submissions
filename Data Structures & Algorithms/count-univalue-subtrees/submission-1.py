# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        max_counter = 0
        def dfs(root, prev):
            nonlocal max_counter 
            if not root:
                return True 
            
            left = dfs(root.left, root)
            right = dfs(root.right, root)
            # Not unitree

            if left and right:
                if root.left and (root.left.val != root.val):
                    return False 
                elif root.right and (root.right.val != root.val):
                    return False 
                else:
                    max_counter += 1
                    return True


        dfs(root, root)
        return max_counter
            
            
        