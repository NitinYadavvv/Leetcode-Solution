# Last updated: 12/10/2025, 8:21:44 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        di = [0]
        def res(root,di):
            if root is None:
                return 0
            l = res(root.left,di)
            r = res(root.right,di)
            
            di[0] = max(di[0],l+r)

            return max(l,r)+1
        res(root,di)
        return di[0]
        
        