# Last updated: 12/10/2025, 11:34:11 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def maxPathSum(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        self.sum = root.val 
14        def helper(root):
15            if root is None:
16                return 0
17            
18            l = max(helper(root.left),0)
19            r = max(helper(root.right),0)
20            self.sum = max(self.sum,l+r+root.val)
21
22            return max(l,r)+root.val
23        helper(root)
24        return self.sum
25
26        