# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """
        root: of binary tree
        task: return max avg value of a subtree of that tree 

        AGAIN: we use a double dfs structure: 1 dfs to traverse anotehr to find the average :) 
        """

        def find_avg(root):
            if not root:
                return 0,0
            
            left_total, left_count = find_avg(root.left)
            right_total, right_count = find_avg(root.right)

            total = (left_total + right_total + root.val)
            count = left_count + right_count + 1
            return total, count

        max_avg = 0
        def dfs(root):
            nonlocal max_avg
            if not root:
                return None 
            
            total, count = find_avg(root)
            if count != 0:
                max_avg = max(max_avg, (total/count))
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return max_avg


        