# Last updated: 12/10/2025, 8:20:45 AM
class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """

        x = []
        while n:
            num = n%10
            if num != 0:
                x.append(num)
            n//=10
        sum = 0
        final = 0
        for i in x[::-1]:
            final = (final*10)  + i 
            sum+=i
        return final * sum 
            
        
        