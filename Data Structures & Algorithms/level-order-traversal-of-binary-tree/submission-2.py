# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        
        def bfs(root):
            queue = deque([root])
            while queue:
                temp = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node:
                        temp.append(node.val)
                    

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(temp)
        bfs(root)
        return result