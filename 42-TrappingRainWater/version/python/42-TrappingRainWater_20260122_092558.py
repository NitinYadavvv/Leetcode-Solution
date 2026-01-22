# Last updated: 1/22/2026, 9:25:58 AM
'''
Ok so this a two pointer problem where we need to make L and R
will move L inwards if R is greater and R inwards if L is greater and calculate L_max and R_max and subract them with the L and R to calculate the water
'''

1class Solution:
2    def trap(self, height: List[int]) -> int:
3        L = 0
4        L_max = height[0]
5        R = len(height)-1
6        R_max = height[R]
7        ans = 0
8        while L!=R:
9
10            if height[L]<=height[R]:
11                L_max = max(L_max,height[L])
12                water = L_max - height[L]
13                ans+=water
14                L+=1
15            else:
16                R_max = max(R_max,height[R])
17                water = R_max - height[R]
18                ans+=water
19                R-=1
20        return ans
21            
22
23
24
25
26
27