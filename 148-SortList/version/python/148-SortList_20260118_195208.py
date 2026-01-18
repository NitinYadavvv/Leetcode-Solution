# Last updated: 1/18/2026, 7:52:08 PM
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
12        def merge(L, R):
13            dummy = ListNode()
14            tail = dummy
15
16            while L and R:
17                if L.val <= R.val:
18                    tail.next = L
19                    L = L.next
20                else:
21                    tail.next = R
22                    R = R.next
23                tail = tail.next
24
25            tail.next = L or R
26            return dummy.next
27
28        def middle(head):
29            fast = head
30            slow = head
31
32            while fast.next and fast.next.next:
33                fast = fast.next.next
34                slow = slow.next
35            
36            return slow 
37        
38        def divide(head):
39
40            if not head or not head.next:
41                return head
42            
43            mid = middle(head)
44            second = mid.next
45            mid.next = None
46
47            L = divide(head)
48            R = divide(second)
49
50            return merge(L,R)
51        
52
53        
54        if not head or not head.next:
55            return head
56        return divide(head)
57