# Last updated: 12/10/2025, 8:21:32 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = deque([root])
        res = [[root.val]]
        while q:
            ans = []
            l = len(q)
            for i in range(l):
                node = q.popleft()
                left = node.left
                right = node.right
                if left and right:
                    if (left.val == x or left.val == y) and (right.val == x or right.val == y):
                        return False
                    else:
                        q.append(left)
                        q.append(right)
                        ans.append(left.val)
                        ans.append(right.val)
                else:
                        
                    if left:
                        q.append(left)
                        ans.append(left.val)
                    if right:
                        q.append(right)
                        ans.append(right.val)
            res.append(ans)
        
        for i in res:
            if x in i and y in i:
                return True
        return False
