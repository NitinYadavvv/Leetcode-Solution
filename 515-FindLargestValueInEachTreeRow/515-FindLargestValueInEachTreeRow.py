# Last updated: 12/10/2025, 8:21:47 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            m = q[0].val
            l = len(q)
            for i in range(l):
                node = q.popleft()
                m = max(m,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(m)
        return res