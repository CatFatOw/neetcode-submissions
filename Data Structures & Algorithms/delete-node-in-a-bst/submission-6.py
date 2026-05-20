# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def search_tree(root, arr, key):
            if not root:
                return arr 
            
            if root.val != key:
                arr.append(root.val)
            
            search_tree(root.left, arr, key)
            search_tree(root.right, arr, key)
            return arr 

        tree_nodes = search_tree(root, [], key)


        # Now reconstruct the BST tree !
        arr = sorted(tree_nodes)
        def reconstruct_bst(arr):
            if not arr:
                return None 
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = reconstruct_bst(arr[:mid])
            root.right = reconstruct_bst(arr[mid+1:])
            return root 
        return reconstruct_bst(arr)
            