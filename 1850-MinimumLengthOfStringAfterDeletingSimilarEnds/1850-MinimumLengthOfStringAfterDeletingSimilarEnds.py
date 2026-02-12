# Last updated: 2/12/2026, 10:51:44 PM
class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s)-1
        while i<j and s[i] == s[j]:
            var = s[i]
            while i<=j and s[i] == var:
                i+=1
            while i<=j and s[j] == var:
                j-=1
        return j-i+1