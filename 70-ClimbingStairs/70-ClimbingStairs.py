# Last updated: 1/18/2026, 6:21:50 PM
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n
        
        lasts = 2
        last = 3
        ans = 0
        for i in range(4,n+1):
            ans = lasts + last
            lasts = last
            last = ans
        return ans