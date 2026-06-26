class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, p, q):
            if not root:
                return None 
            
            if root.val == p.val or root.val == q.val:
                return root 
                
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left and right:
                return root
            return left or right
        return dfs(root, p, q)