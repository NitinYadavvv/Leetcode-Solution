# Last updated: 12/23/2025, 6:34:32 PM
# just a like fibbonacci series if you clearly see the testcases you will observed till 3 only the n is return so we will take two variable and keep updating them as last second and last
1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        if n<4:
8            return n
9        
10        lasts = 2
11        last = 3
12        ans = 0
13        for i in range(4,n+1):
14            ans = lasts + last
15            lasts = last
16            last = ans
17        return ans