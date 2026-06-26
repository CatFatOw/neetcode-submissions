# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(root):
            queue = deque([root])
            result = []
            temp = []
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    temp.append(node)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(temp[-1].val)
                temp = []
            return result 
        return bfs(root)


                


            



        