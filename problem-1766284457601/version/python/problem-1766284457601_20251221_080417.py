# Last updated: 12/21/2025, 8:04:17 AM
1class Solution(object):
2    def mirrorDistance(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        reversed_num = int(str(n)[::-1])
8        return abs(n-reversed_num)
9        