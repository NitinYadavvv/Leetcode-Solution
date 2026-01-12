# Last updated: 1/12/2026, 11:24:59 PM
class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        for i in range(k-1,-1,-1):
            ans+=s[i]
        for i in range(k,len(s)):
            ans+=s[i]
        return ans