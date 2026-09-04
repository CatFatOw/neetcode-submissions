# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        given root
        return the zigzag level order traversal

        left to right then right to left etc

        Example:
        1
        [3,2]
        [4,5,6,7]
        """
        def bfs(root):
            if not root:
                return []
            result = []
            queue = deque([root])
            counter = 0

            while queue:
                temp_len = len(queue)
                temp = []
                for _ in range(temp_len):
                    node = queue.popleft()
                    temp.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                if counter % 2 == 0:
                    result.append(temp)
                else:
                    result.append(temp[::-1])
                counter += 1
            return result
        return bfs(root)
            


        