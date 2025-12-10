# Last updated: 12/10/2025, 8:21:43 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if root is None:
            return []

        q = deque([root])
        res = []
        while q:
            level = len(q)
            avg = 0
            for i in range(level):
                node=q.popleft()
                avg+=float(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            avg = avg/level
            res.append(avg)

        return res