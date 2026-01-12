# Last updated: 1/12/2026, 11:26:50 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        h = {}
        h[None] = None
        while curr:
            h[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            h[curr].next = h[curr.next]

            h[curr].random = h[curr.random]
            curr = curr.next
        return h[head]

            

        