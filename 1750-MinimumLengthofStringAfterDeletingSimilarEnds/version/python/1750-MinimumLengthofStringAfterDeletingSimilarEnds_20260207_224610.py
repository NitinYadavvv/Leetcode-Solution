# Last updated: 2/7/2026, 10:46:10 PM
1class Solution:
2    def minimumLength(self, s: str) -> int:
3        i = 0
4        j = len(s)-1
5        while i<j and s[i] == s[j]:
6            var = s[i]
7            while i<=j and s[i] == var:
8                i+=1
9            while i<=j and s[j] == var:
10                j-=1
11        return j-i+1