# Last updated: 1/18/2026, 6:21:43 PM
class Solution(object):
    def minWindow(self, s, t):
        dict = {}
        for ch in t:
            dict[ch] = dict.get(ch, 0) + 1

        required = len(dict)
        i = j = c = 0
        ans = float('inf')
        res = ''

        while j < len(s):
            if s[j] in dict:
                dict[s[j]] -= 1
                if dict[s[j]] == 0:
                    c += 1

            while c == required:
                if j - i + 1 < ans:
                    ans = j - i + 1
                    res = s[i:j+1]

                if s[i] in dict:
                    dict[s[i]] += 1
                    if dict[s[i]] == 1:
                        c -= 1
                i += 1

            j += 1

        return res
