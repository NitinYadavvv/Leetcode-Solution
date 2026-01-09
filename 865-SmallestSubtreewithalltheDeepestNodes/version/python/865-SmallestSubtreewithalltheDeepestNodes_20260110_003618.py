# Last updated: 1/10/2026, 12:36:18 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution(object):
9    def subtreeWithAllDeepest(self, root):
10        """
11        :type root: Optional[TreeNode]
12        :rtype: Optional[TreeNode]
13        """
14
15        def helper(node, d):
16            if node is None:
17                return (d - 1, None)
18
19            ld, ln = helper(node.left, d + 1)
20            rd, rn = helper(node.right, d + 1)
21
22            if ld == rd:
23                return (ld, node)
24            elif ld > rd:
25                return (ld, ln)
26            else:
27                return (rd, rn)
28
29        ans = helper(root, 0)
30        return ans[1]
31