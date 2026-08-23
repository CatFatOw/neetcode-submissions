# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque 
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        mapping = defaultdict(list)

        def dfs(root):
            if not root:
                return None 
            
            if root.left:
                mapping[root].append(root.left)
                mapping[root.left].append(root)
            
            if root.right:
                mapping[root].append(root.right)
                mapping[root.right].append(root)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)


        def bfs(root):
            queue = deque([(root, None, 1)])
            visited = set([root])
            max_length = 1
            while queue:
                node, prev, length = queue.popleft()
                if prev in visited:
                    if abs(node.val - prev.val) == 1:
                        length +=1
                    else:
                        length = 1
                max_length = max(max_length, length)
                
                for neighbor in mapping[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node, length))
            return max_length
        ans = 1
        for node in mapping.keys():
            result = bfs(node)
            ans = max(ans, result)
        return ans
        