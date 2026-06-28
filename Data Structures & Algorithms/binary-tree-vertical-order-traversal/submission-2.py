# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bfs(root, col):
            mapping = defaultdict(list)
            queue = deque([(root,col)])
            while queue:
                node, col = queue.popleft()
                mapping[col].append(node.val)
                if node.left:
                    queue.append((node.left, col-1))
                if node.right:
                    queue.append((node.right, col+1))
            return mapping 
        mapping = bfs(root, 1)

        return [mapping[col] for col in sorted(mapping)]
        