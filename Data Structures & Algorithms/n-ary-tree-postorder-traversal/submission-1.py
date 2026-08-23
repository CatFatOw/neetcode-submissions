"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        Appraoch:
        use a version of DFS that does postorder traversal

        """
        result = []
        def dfs(root):
            if not root:
                return None 
            
            for children in root.children:
                dfs(children)
            result.append(root.val)
        dfs(root)
        return result
        