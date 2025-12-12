# Last updated: 12/12/2025, 9:05:32 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.sum = root.val 
        def helper(root):
            if root is None:
                return 0
            
            l = max(helper(root.left),0)
            r = max(helper(root.right),0)
            self.sum = max(self.sum,l+r+root.val)

            return max(l,r)+root.val
        helper(root)
        return self.sum

        