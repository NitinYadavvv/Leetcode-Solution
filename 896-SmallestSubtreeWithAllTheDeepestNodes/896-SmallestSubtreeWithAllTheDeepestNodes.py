# Last updated: 1/12/2026, 11:25:43 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def helper(node, d):
            if node is None:
                return (d - 1, None)

            ld, ln = helper(node.left, d + 1)
            rd, rn = helper(node.right, d + 1)

            if ld == rd:
                return (ld, node)
            elif ld > rd:
                return (ld, ln)
            else:
                return (rd, rn)

        ans = helper(root, 0)
        return ans[1]
