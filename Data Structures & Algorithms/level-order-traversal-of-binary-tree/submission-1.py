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

        def bfs(root):
            result = []
            queue = deque([root])
            
            while queue:
                path_nodes = []
                n_nodes = len(queue)

                for _ in range(n_nodes):
                    node = queue.popleft()
                    path_nodes.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(path_nodes)
            return result 
        return bfs(root) 


        