# Last updated: 1/30/2026, 11:25:10 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        c = 0
4        for i in range(32):
5            if n & (1<<i):
6                c+=1
7        return c