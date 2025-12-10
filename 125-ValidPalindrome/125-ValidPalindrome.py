# Last updated: 12/10/2025, 8:22:51 AM
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = s.lower()
        t = re.sub(r'[^a-z0-9]','',t)
        check = t
        t = t[::-1]
        return check == t

        