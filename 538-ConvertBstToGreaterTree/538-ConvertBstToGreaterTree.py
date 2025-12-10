# Last updated: 12/10/2025, 8:21:46 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.total = 0
        
        def ans(root):

            if root is None:
                return 
            ans(root.right)
            root.val+=self.total
            self.total = root.val
            ans(root.left)
        
        ans(root)
        return root
            
            
        
        