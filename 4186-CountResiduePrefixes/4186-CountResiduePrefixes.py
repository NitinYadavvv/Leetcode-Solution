# Last updated: 1/12/2026, 11:24:58 PM
class Solution(object):
    def residuePrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        for i in range(1,len(s)):
            t = set()
            for j in range(i+1):
                t.add(s[j])
            if len(s[0:i+1])%3 == len(t):
                ans+=1
        return ans
        