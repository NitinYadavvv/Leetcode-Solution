# Last updated: 12/10/2025, 8:24:28 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s.strip()
        for i in range(len(s)):
            if s[i] == ' ':
                count = 0
            else:
                count+=1
        return count 
        