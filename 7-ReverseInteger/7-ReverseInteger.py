# Last updated: 12/10/2025, 8:25:08 AM
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = ""
        if x < 0:
            x = abs(x)
            n = "-"
        s = str(x)
        s = s[::-1]
        num = int(n+s)
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num
        