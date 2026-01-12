# Last updated: 1/12/2026, 11:25:33 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = deque([root])
        res = 0
        level = 1
        min = root.val
        while q:
            
            sum = 0
            l = len(q)
            for i in range(l):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if min<sum:
                res = level
                min = sum
            level+=1
        if res == 0:
            return 1
        return res
        