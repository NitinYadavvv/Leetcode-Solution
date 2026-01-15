# Last updated: 1/15/2026, 6:00:24 PM
# xor it both the numbers then count the number of 1s
1class Solution:
2    def minBitFlips(self, start: int, goal: int) -> int:
3        ans = start ^ goal  
4        c = 0
5        for i in range(31):
6            n = 1<<i
7            if ans & n:
8                c+=1
9        return c
10        