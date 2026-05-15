# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        def bfs(root):
            queue = deque([root])
            result = []
            counter = 0
            while queue:
                n_nodes = len(queue)
                if counter % 2 != 0:
                    level_nodes = [x.val for x in reversed(queue)]
                else:
                    level_nodes = [x.val for x in queue]
                counter += 1
                result.append(level_nodes)

                for _ in range(n_nodes):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return result 
        return bfs(root)


        