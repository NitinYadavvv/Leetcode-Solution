# Last updated: 1/18/2026, 6:17:50 PM
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal  
        c = 0
        for i in range(31):
            n = 1<<i
            if ans & n:
                c+=1
        return c
        