# Last updated: 12/10/2025, 8:21:23 AM
class Solution(object):
    def numSub(self, s):
        MOD = 10**9 + 7
        ans = 0
        cur = 0

        for c in s:
            if c == '1':
                cur += 1
                ans = (ans + cur) % MOD
            else:
                cur = 0

        return ans
