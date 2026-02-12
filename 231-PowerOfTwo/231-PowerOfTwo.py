# Last updated: 2/12/2026, 10:52:31 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
          return n > 0 and (n & (n - 1)) == 0
        