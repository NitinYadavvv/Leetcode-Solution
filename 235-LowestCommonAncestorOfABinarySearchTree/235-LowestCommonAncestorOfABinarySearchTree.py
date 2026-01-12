# Last updated: 1/12/2026, 11:26:29 PM
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
        
        if p == root:
            return root
        if q == root:
            return root

        if (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
            return root
        
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)

        if l:
            return l
        if r:
            return r

