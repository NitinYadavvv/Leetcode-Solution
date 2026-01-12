# Last updated: 1/12/2026, 11:26:58 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        self.ans = 0
        self.r = False
        def res(root):
            if root is None:
                return 0
            
            l = res(root.left)
            r = res(root.right)

            self.ans = l-r
            if self.ans > 1 or self.ans <-1:
                self.r = True
            return max(l,r)+1
        
        res(root)
        if self.r:
            return False
        
        return True