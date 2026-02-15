# Last updated: 2/15/2026, 8:31:10 AM
1class Solution:
2    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
3        h = {}
4        for i in bulbs:
5            if i not in h:
6                h[i] = 1
7            else:
8                if h[i] == 1:
9                    h[i] = 0
10                else:
11                    h[i] = 1
12
13        ans = []
14        for i in h:
15            if h[i] == 1:
16                ans.append(i)
17        ans.sort()
18        return ans