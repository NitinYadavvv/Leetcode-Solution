# Last updated: 12/10/2025, 8:22:05 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    
        if root is None:
            return
        
        if root == p:
            return root
        if root == q:
            return root
        
        p1 = self.lowestCommonAncestor(root.left,p,q)
        p2 = self.lowestCommonAncestor(root.right,p,q)

        if p1 and p2:
            return root
        if p1:
            return p1
        if p2:
            return p2
    
    
