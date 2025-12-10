# Last updated: 12/10/2025, 8:23:22 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q = deque()
        
        q.append(root.left)
        
        q.append(root.right)
        while q:
            node = q.popleft()
            node1 = q.popleft()
            if not node and not node1:
                continue
            if not node or not node1:
                return False
            if node.val != node1.val:
                return False
            q.append(node.left)
            
            q.append(node1.right)
            
            q.append(node.right)
            
            q.append(node1.left)



        return True
            
        







         
             
        