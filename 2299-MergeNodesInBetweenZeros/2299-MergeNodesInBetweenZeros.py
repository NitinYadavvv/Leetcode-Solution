# Last updated: 12/10/2025, 8:21:10 AM
class Solution(object):
    def mergeNodes(self, head):
        t = head.next
        i = head.next

        while t:
            s = 0
            while t.val != 0:
                s += t.val
                t = t.next

            i.val = s
            i.next = t.next
            i = t.next
            t = t.next

        return head.next
