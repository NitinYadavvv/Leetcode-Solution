# Last updated: 12/22/2025, 10:51:42 PM
# in this first we will make every single node copy just by the value after that we keep them in hash then again do a pass and match next and random pointer
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x, next=None, random=None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution(object):
11    def copyRandomList(self, head):
12        """
13        :type head: Node
14        :rtype: Node
15        """
16        curr = head
17        h = {}
18        h[None] = None
19        while curr:
20            h[curr] = Node(curr.val)
21            curr = curr.next
22        
23        curr = head
24        while curr:
25            h[curr].next = h[curr.next]
26
27            h[curr].random = h[curr.random]
28            curr = curr.next
29        return h[head]
30
31            
32
33        