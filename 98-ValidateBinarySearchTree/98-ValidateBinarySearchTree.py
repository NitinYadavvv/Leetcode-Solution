# Last updated: 12/10/2025, 8:23:33 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root,L,H):
            if root is None:
                return True
            
            if L!= None and root.val<=L:
                return False

            if H!= None and root.val>=H:
                return False
            
            left = helper(root.left,L,root.val)

            right = helper(root.right,root.val,H)
        
            return left and right

        return helper(root,None,None)       
