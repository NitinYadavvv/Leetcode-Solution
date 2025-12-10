# Last updated: 12/10/2025, 8:23:30 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        t1 = []
        t2 = []
        def res(p,q):
            if not p or not q: 
                t1.append(p)
                t2.append(q)
                return
            
            t1.append(p.val)
            t2.append(q.val)
            res(p.left,q.left)
            res(p.right,q.right)
        
        res(p,q)
        print(t1)
        print(t2)
        return t1==t2

        
        