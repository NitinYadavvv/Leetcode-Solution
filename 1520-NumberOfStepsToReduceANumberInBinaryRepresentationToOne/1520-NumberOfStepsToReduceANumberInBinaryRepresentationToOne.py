# Last updated: 2/26/2026, 7:47:58 AM
class Solution:
    def numSteps(self, s: str) -> int:
    
        ans = int(s,2)
        res = 0
        while ans!=1:
            res+=1
            if ans%2 == 0:
                ans//=2
            else:
                ans+=1
        return res
