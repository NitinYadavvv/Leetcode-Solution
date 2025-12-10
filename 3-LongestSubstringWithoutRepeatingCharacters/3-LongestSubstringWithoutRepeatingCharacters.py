# Last updated: 12/10/2025, 8:25:11 AM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        i = 0
        j = 0
        r = 0
        while j<len(s):
            if s[j] not in res:
                res.add(s[j])
                j+=1
                r = max(r,len(res))
            else:
                res.remove(s[i])
                i+=1
        return r
        
            
               
