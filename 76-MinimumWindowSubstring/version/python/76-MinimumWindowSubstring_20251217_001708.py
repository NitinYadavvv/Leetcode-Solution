# Last updated: 12/17/2025, 12:17:08 AM
# timepass
1class Solution(object):
2    def minWindow(self, s, t):
3        dict = {}
4        for ch in t:
5            dict[ch] = dict.get(ch, 0) + 1
6
7        required = len(dict)
8        i = j = c = 0
9        ans = float('inf')
10        res = ''
11
12        while j < len(s):
13            if s[j] in dict:
14                dict[s[j]] -= 1
15                if dict[s[j]] == 0:
16                    c += 1
17
18            while c == required:
19                if j - i + 1 < ans:
20                    ans = j - i + 1
21                    res = s[i:j+1]
22
23                if s[i] in dict:
24                    dict[s[i]] += 1
25                    if dict[s[i]] == 1:
26                        c -= 1
27                i += 1
28
29            j += 1
30
31        return res
32