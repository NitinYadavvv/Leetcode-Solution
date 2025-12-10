# Last updated: 12/10/2025, 8:22:26 AM
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        sum = 0
        while n!=1 and n not in seen:
            seen.add(n)
            sum = 0
            while n:
                sum+=(n%10)**2
                n=n//10
            n = sum 
        return n==1
             
            






        