# Last updated: 12/10/2025, 8:22:48 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.sum = 0
        s = ''
        def helper(root,s):
            if root is None:
                return 
            s+=str(root.val)
            if not root.left and not root.right:
                self.sum+=int(s)
                return

            helper(root.left,s)
            helper(root.right,s)
        helper(root,s)
        return self.sum
        