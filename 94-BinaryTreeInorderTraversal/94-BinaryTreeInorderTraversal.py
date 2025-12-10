# Last updated: 12/10/2025, 8:23:40 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.ans(root,[])
    def ans(self,root,res):
        if root is None:
            return res
        res = self.ans(root.left,res)
        res.append(root.val)
        res = self.ans(root.right,res)
        return res