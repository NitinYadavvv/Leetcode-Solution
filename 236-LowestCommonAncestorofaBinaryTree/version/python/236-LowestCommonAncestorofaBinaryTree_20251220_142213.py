# Last updated: 12/20/2025, 2:22:13 PM
# so same as the LCA of binary tree the only diffrence is we got found early that our p and q lies in left or right subtree cause its a binary tree so we just simpy check if p is in left and q is in right then the root is our answer or if p in right and q in left then also root is our answer if both not satisfy just go in left then right and if you find your p or q just return it
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution(object):
9    def lowestCommonAncestor(self, root, p, q):
10        """
11        :type root: TreeNode
12        :type p: TreeNode
13        :type q: TreeNode
14        :rtype: TreeNode
15        """
16        if root is None:
17            return 
18        
19        if p == root:
20            return root
21        if q == root:
22            return root
23
24        if (p.val<root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
25            return root
26        
27        l = self.lowestCommonAncestor(root.left,p,q)
28        r = self.lowestCommonAncestor(root.right,p,q)
29
30        if l:
31            return l
32        if r:
33            return r
34
35