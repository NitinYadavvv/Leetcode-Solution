# Last updated: 12/10/2025, 8:22:55 AM
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return
        q = deque([root])
        res = []
        while q:
            s = len(q)
            for i in range(s):
                node = q.popleft()
                if q and i<s-1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return root  