# Last updated: 12/10/2025, 8:20:51 AM
class Solution(object):
    def decimalRepresentation(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        st = str(n)
        st = st[::-1]
        l = len(st)-1
        n = int(st)
        a = []
        while l>=0:
            num = n%10
            if num!= 0:
                a.append(num*(10**l))
            n = n/10
            l-=1
        return a
            
            
        
            
            