# Last updated: 12/10/2025, 8:20:46 AM
class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        so = set()
        for i in range(len(s)):
            so.add(s[i])
        return len(so)