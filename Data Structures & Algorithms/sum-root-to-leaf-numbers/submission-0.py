# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        def dfs(root, num):
            if not root:
                return 
            num += str(root.val)
            if not root.left and not root.right:
                result.append(int(num))
            
            dfs(root.left,num)
            dfs(root.right, num)
        dfs(root, "")
        #print(result)
        return sum(result)

        
            
            
            
            
            
        