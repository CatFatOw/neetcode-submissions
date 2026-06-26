# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def delete_bst(root, key):
            if not root:
                return None 
            
            if root.val < key:
                root.right = delete_bst(root.right, key)
            elif root.val > key:
                root.left = delete_bst(root.left, key)
            else:
                # delete this node
                        
                # Basically deleting if its a single node :)
                if not root.left:
                    return root.right 
                if not root.right:
                    return root.left

                curr = root.right
                while curr.left:
                    curr = curr.left 

                root.val = curr.val
                # reassign the root w/ curr    
                
                # now we must delete curr 
                root.right = delete_bst(root.right, curr.val)
            return root
        return delete_bst(root, key)
