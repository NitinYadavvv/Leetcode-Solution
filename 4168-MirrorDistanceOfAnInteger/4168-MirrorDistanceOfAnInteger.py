# Last updated: 1/12/2026, 11:25:02 PM
class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        reversed_num = int(str(n)[::-1])
        return abs(n-reversed_num)
        