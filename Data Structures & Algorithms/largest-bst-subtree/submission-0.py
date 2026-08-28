# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """
        given binary tree, find the largest subtree (mosst amount of nodes), that is also a valid BST 

        APPROACH:
        double bfs, we start at each node (traverse via dfs) and then at each node we run a is_valid checker and then if true we return that root 

        """

        def is_valid(root, low, high):
            if not root:
                return True 
            
            if low >= root.val or high <= root.val:
                return False 
            
            left = is_valid(root.left, low,root.val)
            right = is_valid(root.right, root.val,high)
            return left and  right
        
        max_size = 0
        def dfs(root):
            if not root:
                return 0
        
            if is_valid(root, float("-inf"), float("inf")):
                return 1 + dfs(root.left) + dfs(root.right)
            else:
               return max(dfs(root.left), dfs(root.right))
        return dfs(root)

            
            

