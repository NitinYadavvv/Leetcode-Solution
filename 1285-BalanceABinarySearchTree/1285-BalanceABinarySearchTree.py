# Last updated: 2/12/2026, 10:51:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inodr = []
        def inorder(root):
            if root is None:
                return 
            
            inorder(root.left)
            self.inodr.append(root.val)
            inorder(root.right)
        
        def make(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            
            mid = len(arr)//2
            Node = TreeNode(arr[mid])
            Node.left = make(arr[0:mid])
            Node.right = make(arr[mid+1:])
            return Node
        inorder(root)
        return make(self.inodr)
        