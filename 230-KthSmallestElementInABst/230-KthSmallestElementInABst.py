# Last updated: 12/10/2025, 8:22:14 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.c = 0
       
        def res(root):
            if root is None:
                return

            res(root.left) 
            self.c+=1
            if self.c == k:
                self.ans = root.val
                return
            res(root.right)
        
        self.ans = 0
        res(root)
        return self.ans
            
        