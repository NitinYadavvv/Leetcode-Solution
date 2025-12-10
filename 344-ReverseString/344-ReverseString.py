# Last updated: 12/10/2025, 8:21:56 AM
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while j>i:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1

        