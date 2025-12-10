# Last updated: 12/10/2025, 8:23:20 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        self.level(root,0,res)
        return res
    def level(self,root,l,res):
        if root is None:
            return
        
        if len(res)<=l:
            res.append([])
        
        res[l].append(root.val)
        self.level(root.left,l+1,res)
        self.level(root.right,l+1,res)
