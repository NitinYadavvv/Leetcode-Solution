# Last updated: 12/10/2025, 8:23:18 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        f  = 1
        q = deque([root])
        res = []
        while q:
            l = len(q)
            curr = []
            if f == 0:
              
                for i in range(l):
                    node = q.pop()
                    curr.append(node.val)
                    if node.right is not None:
                        q.appendleft(node.right)
                    if node.left is  not None:
                        q.appendleft(node.left)
                f=1
            else:
                for i in range(l):
                    node = q.popleft()
                    curr.append(node.val)
                    if node.left is  not None:
                        q.append(node.left)
                    if node.right is  not None:
                        q.append(node.right)
                f = 0
            res.append(curr)
        return res


                
                

        
        