# Last updated: 1/3/2026, 10:47:52 PM
# simple
1class Solution(object):
2    def reversePrefix(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: str
7        """
8        ans = ""
9        for i in range(k-1,-1,-1):
10            ans+=s[i]
11        for i in range(k,len(s)):
12            ans+=s[i]
13        return ans