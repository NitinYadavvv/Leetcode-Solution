# Last updated: 2/12/2026, 10:51:04 PM
class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 1
        i =1
        while 2**i-1 <= n:
            i+=1
            ans+=1
        return ans