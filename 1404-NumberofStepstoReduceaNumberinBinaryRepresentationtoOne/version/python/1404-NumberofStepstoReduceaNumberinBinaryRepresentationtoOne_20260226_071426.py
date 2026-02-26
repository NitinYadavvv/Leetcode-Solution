# Last updated: 2/26/2026, 7:14:26 AM
1class Solution:
2    def numSteps(self, s: str) -> int:
3    
4        ans = int(s,2)
5        res = 0
6        while ans!=1:
7            res+=1
8            if ans%2 == 0:
9                ans//=2
10            else:
11                ans+=1
12        return res
13