# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        def bfs(root):
            queue = deque([root])
            result = []
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    if node:
                        result.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
 
                    else:
                       result.append(None)
                
                
            return result

        result = bfs(root)
        
        seen_null = False

        for x in result:
            if x is None:
                seen_null = True
            else:
                if seen_null:
                    return False

        return True
       