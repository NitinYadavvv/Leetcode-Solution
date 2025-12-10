# Last updated: 12/10/2025, 8:22:15 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return
        
        def res(root):
            if root is None:
                return
            
            res(root.left)
            res(root.right)
            root.left , root.right = root.right , root.left
            
        res(root)
        return root


        