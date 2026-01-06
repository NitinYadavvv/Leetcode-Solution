# Last updated: 1/6/2026, 10:13:29 PM
1class Solution(object):
2    def repeatedNTimes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        h = {}
8        for i in nums:
9            if i in h:
10                return i
11            h[i] = 1