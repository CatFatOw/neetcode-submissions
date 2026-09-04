# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        given root
        return only the right most sides


        APPORACH:

        do BFS
        for each level append the leftmost value 
        """
        
        def bfs(root):
            if not root:
                return []
            result = []
            queue = deque([root])
            
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
                result.append(temp[-1])
            return result 
        return bfs(root)

        