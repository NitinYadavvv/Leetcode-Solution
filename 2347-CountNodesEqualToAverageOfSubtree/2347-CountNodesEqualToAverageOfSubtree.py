# Last updated: 12/10/2025, 8:21:07 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        n = 0
        def node(root):
            if root is None:
                return 0
            return node(root.left)+node(root.right)+1
        def ans(root):
            if root is None:
                return 0
                       
            left = ans(root.left)
            right = ans(root.right)
            avg = (left+right+root.val)//node(root)
            if avg == root.val:
                self.c+=1
            
            return left+right+root.val
        
        self.c = 0
        ans(root)
        return self.c
            

            
        