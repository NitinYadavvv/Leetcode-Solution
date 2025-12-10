# Last updated: 12/10/2025, 8:21:31 AM
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        count = 0
        res = ''
        for i in range(len(s)):
            if s[i] == '(':
                if count > 0:
                    res+='('
                count+=1
            else:
                count-=1
                if count>0:
                    res+=')'
        return res






        
                    




        