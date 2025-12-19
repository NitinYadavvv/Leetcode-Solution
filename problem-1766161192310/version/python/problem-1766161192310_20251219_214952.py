# Last updated: 12/19/2025, 9:49:52 PM
# so basically in this problem i am using a stack in which first i take each node one by one so that if i pop it it will be in reverse order after that i just simply pop each element from the stack add that in the middle of head.next till head and fast will become same
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reorderList(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: None Do not return anything, modify head in-place instead.
11        """
12
13        self.head = head
14        fast = head
15        s = [head]
16        while fast.next:
17            fast = fast.next
18            s.append(fast)
19        
20        fast = s.pop()
21        while fast != self.head and self.head.next != fast:
22            fast.next = self.head.next
23            self.head.next = fast
24            self.head = fast.next
25            fast = s.pop()
26        
27        if self.head.next != fast:
28            self.head.next = None
29        else:
30            fast.next = None
31
32        
33
34
35        