# Last updated: 12/16/2025, 10:36:27 AM
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        h = {}
        freq = 0
        ans = 0
        while j<len(s):
            if s[j] not in h:
                h[s[j]] = 1
            else:
                h[s[j]]+=1
            freq = max(h.values())
            if (j-i+1) - freq <=k:
                ans = max(j-i+1,ans)
                j+=1
            else:
                h[s[i]]-=1
                h[s[j]]-=1
                i+=1
        return ans
            
        