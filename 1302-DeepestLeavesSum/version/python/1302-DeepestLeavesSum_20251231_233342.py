# Last updated: 12/31/2025, 11:33:42 PM
# simple BFS keep recording every level then return the sum of the last level by doing sum(ans(-1))
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7from collections import deque
8class Solution(object):
9    def deepestLeavesSum(self, root):
10        """
11        :type root: Optional[TreeNode]
12        :rtype: int
13        """
14        q = deque([root])
15        ans = []
16        while q:
17            l = []
18            for i in range(len(q)):
19                node = q.popleft()
20                l.append(node.val)
21                if node.left:
22                    q.append(node.left)
23                if node.right:
24                    q.append(node.right)
25            ans.append(l)
26        return sum(ans[-1])