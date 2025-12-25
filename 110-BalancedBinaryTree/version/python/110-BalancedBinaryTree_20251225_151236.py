# Last updated: 12/25/2025, 3:12:36 PM
# check left subtree hight then right subtree do L-R
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isBalanced(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        
14        self.ans = 0
15        self.r = False
16        def res(root):
17            if root is None:
18                return 0
19            
20            l = res(root.left)
21            r = res(root.right)
22
23            self.ans = l-r
24            if self.ans > 1 or self.ans <-1:
25                self.r = True
26            return max(l,r)+1
27        
28        res(root)
29        if self.r:
30            return False
31        if self.ans > 1 or self.ans <-1:
32            return False
33        return True