# Last updated: 1/14/2026, 11:05:41 PM
1class Solution(object):
2    def findMiddleIndex(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        left = 0
8        right = 0
9
10        left = sum(nums)    
11        for i in range(len(nums)):
12         
13            left-=nums[i]
14            if left == right:
15                return i
16            right+=nums[i]
17
18        return -1
19        