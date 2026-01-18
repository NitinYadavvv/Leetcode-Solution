# Last updated: 1/18/2026, 7:50:26 PM
# perform merge sort
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def sortList(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: Optional[ListNode]
11        """
12        
13        def merge(L,R):
14            i = L
15            j = R
16            ll = ListNode()
17            last = ll
18
19            while i and j:
20                if i.val >= j.val:
21                    last.next = ListNode(j.val)
22                    last = last.next
23                    j = j.next
24                else:
25                   last.next = ListNode(i.val)
26                   last = last.next
27                   i=i.next 
28            while i:
29                last.next = ListNode(i.val)
30                last = last.next
31                i=i.next
32            while j:
33                last.next = ListNode(j.val)
34                last = last.next
35                j = j.next
36            
37            return ll.next
38        def middle(head):
39            fast = head
40            slow = head
41
42            while fast.next and fast.next.next:
43                fast = fast.next.next
44                slow = slow.next
45            
46            return slow 
47        
48        def divide(head):
49
50            if not head or not head.next:
51                return head
52            
53            mid = middle(head)
54            second = mid.next
55            mid.next = None
56
57            L = divide(head)
58            R = divide(second)
59
60            return merge(L,R)
61        
62
63        
64        if not head or not head.next:
65            return head
66        return divide(head)
67 
68
69
70                