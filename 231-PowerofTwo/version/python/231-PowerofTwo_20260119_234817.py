# Last updated: 1/19/2026, 11:48:17 PM
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3          return n > 0 and (n & (n - 1)) == 0
4        