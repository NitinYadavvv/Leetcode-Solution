# Last updated: 2/9/2026, 7:36:08 AM
# use stack
1class Solution:
2    def mergeAdjacent(self, nums: List[int]) -> List[int]:
3        
4
5        stack = []
6        for i in nums:
7            stack.append(i)
8            while len(stack)>1 and stack[-2] == stack[-1]:
9                v = stack.pop()
10                stack.pop()
11                stack.append(v*2)
12        return stack