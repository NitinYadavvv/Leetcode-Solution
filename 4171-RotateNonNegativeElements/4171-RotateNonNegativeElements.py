# Last updated: 2/12/2026, 10:51:08 PM
from collections import deque
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        pos = []
        for i in range(len(nums)):
            if nums[i]>=0:
                q.append(nums[i])
                pos.append(i)

        if len(q) == 0:
            return nums
        for i in range(k):
            var  = q.popleft()
            q.append(var)

        for i in range(len(pos)):
            nums[pos[i]] = q[i]
        return nums
            