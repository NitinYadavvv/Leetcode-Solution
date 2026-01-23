# Last updated: 1/23/2026, 10:44:48 PM
# so easy
1class Solution:
2    def rearrangeArray(self, nums: List[int]) -> List[int]:
3        pos = []
4        neg = []
5
6        for i in nums:
7            if i>0:
8                pos.append(i)
9            else:
10                neg.append(i)
11        
12        res = []
13        for i in range(len(pos)):
14            res.append(pos[i])
15            res.append(neg[i])
16        return res