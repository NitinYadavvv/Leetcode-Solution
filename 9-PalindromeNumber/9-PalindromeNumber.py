# Last updated: 12/10/2025, 8:25:04 AM
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        x=s[::-1]
        if s == x:
            return True
        return False
