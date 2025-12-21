# Last updated: 12/21/2025, 8:49:21 AM
1class Solution(object):
2    def minCost(self, s, cost):
3        """
4        :type s: str
5        :type cost: List[int]
6        :rtype: int
7        """
8        m = sum(cost)
9        h = {}
10        for i in range(len(s)):
11            if s[i] in h:
12                h[s[i]] += cost[i]
13            else:
14                h[s[i]] = cost[i]
15        return m - max(h.values())
16            
17          