# Last updated: 12/10/2025, 8:20:50 AM
class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        res = ''
        for i in s:
            if i != '0':
                res+=i
        return int(res)
                
            
        
        