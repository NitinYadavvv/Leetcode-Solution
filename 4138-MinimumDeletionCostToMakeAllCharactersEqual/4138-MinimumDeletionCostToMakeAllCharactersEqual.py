# Last updated: 1/12/2026, 11:25:03 PM
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        m = sum(cost)
        h = {}
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]] += cost[i]
            else:
                h[s[i]] = cost[i]
        return m - max(h.values())
            
          