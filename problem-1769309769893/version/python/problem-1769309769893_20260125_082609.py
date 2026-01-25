# Last updated: 1/25/2026, 8:26:09 AM
1from collections import deque
2class Solution:
3    def rotateElements(self, nums: List[int], k: int) -> List[int]:
4        q = deque()
5        pos = []
6        for i in range(len(nums)):
7            if nums[i]>=0:
8                q.append(nums[i])
9                pos.append(i)
10
11        if len(q) == 0:
12            return nums
13        for i in range(k):
14            var  = q.popleft()
15            q.append(var)
16
17        for i in range(len(pos)):
18            nums[pos[i]] = q[i]
19        return nums
20            