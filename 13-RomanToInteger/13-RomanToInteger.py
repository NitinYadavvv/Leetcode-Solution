# Last updated: 12/10/2025, 8:24:57 AM
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res = 0
        i=0
        while len(s) > i:
            if i+1 < len(s) and  roman[s[i]] < roman[s[i+1]]:
                res += roman[s[i+1]] - roman[s[i]]
                i+=2
            else:
                res+=roman[s[i]]
                i+=1

        return res
        