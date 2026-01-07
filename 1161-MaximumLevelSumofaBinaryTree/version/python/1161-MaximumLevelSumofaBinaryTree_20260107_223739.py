# Last updated: 1/7/2026, 10:37:39 PM
# run BFS and easy you know about it
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution(object):
9    def maxLevelSum(self, root):
10        """
11        :type root: Optional[TreeNode]
12        :rtype: int
13        """
14        q = deque([root])
15        res = 0
16        level = 1
17        min = root.val
18        while q:
19            
20            sum = 0
21            l = len(q)
22            for i in range(l):
23                node = q.popleft()
24                sum += node.val
25                if node.left:
26                    q.append(node.left)
27                if node.right:
28                    q.append(node.right)
29            
30            if min<sum:
31                res = level
32                min = sum
33            level+=1
34        if res == 0:
35            return 1
36        return res
37        