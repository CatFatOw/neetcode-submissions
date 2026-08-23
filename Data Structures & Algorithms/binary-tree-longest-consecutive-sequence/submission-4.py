# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
        return the longest consecutive sequence path (increase by 1)

        APPORACH: 
        normal DFS but keep track of the prev.

        if its not consecutive increasing then restart at that specific node 
        """
        if not root:
            return 0

        max_sequence = 1
        

        def dfs(root,prev, curr_length):
            nonlocal max_sequence
            if not root:
                return 0

            if root.val - prev == 1:
                curr_length += 1
            else:
                curr_length = 1
            max_sequence = max(max_sequence, curr_length)

            
            left = dfs(root.left, root.val,curr_length)
            right = dfs(root.right,root.val, curr_length)
        dfs(root, root.val, 0)
        return max_sequence


        