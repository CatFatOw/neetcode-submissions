# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """
        given the root of a binary tree, return the number of uni-value subtrees

        uni-value subtree means all node values in the subtree are the same

        EXAMPLES:
            root = [5,1,5,5,5,null,5]
            4 univalue subtree

        APPORACH:
        do a dfs at a start root to check if they have the same values 
        return True/False

        then traverse through each node and then append 1 by that 

        """
        def is_unitree(root, val):
            if not root:
                return True 
            
            if root.val != val:
                return False 
            
            left = is_unitree(root.left, val)
            right = is_unitree(root.right, val)
            return left and right
        
        # now we traverse through the entire tree 
        total = 0
        def dfs(root):
            nonlocal total
            if not root:
                return None 
            if is_unitree(root, root.val):
                total += 1
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return total

        