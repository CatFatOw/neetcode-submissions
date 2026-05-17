# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.candidate = root.val 
        def find_candidate(root, target):
            if not root:
                return None 
            
            difference = abs(root.val - target)
            if difference < abs(self.candidate - target):
                self.candidate = root.val
            find_candidate(root.left, target)
            find_candidate(root.right, target)
        find_candidate(root, target)
        return self.candidate
            