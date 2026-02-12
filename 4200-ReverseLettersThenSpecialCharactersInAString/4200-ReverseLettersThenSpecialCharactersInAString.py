# Last updated: 2/12/2026, 10:51:01 PM
class Solution:
    def reverseByType(self, s: str) -> str:
        ch = []
        sp = []
        arr = [0]*len(s)
        for i in range(len(s)):
            if s[i].isalpha():
                arr[i] = 1
                ch.append(s[i])
            else:
                sp.append(s[i])
        ans = ''
        for i in range(len(arr)):
            if arr[i] == 1:
                ans+=ch.pop()
            else:
                ans+=sp.pop()
        return ans