# Last updated: 1/11/2026, 8:10:15 AM
1class Solution(object):
2    def residuePrefixes(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        ans = 1
8        for i in range(1,len(s)):
9            t = set()
10            for j in range(i+1):
11                t.add(s[j])
12            if len(s[0:i+1])%3 == len(t):
13                ans+=1
14        return ans
15        