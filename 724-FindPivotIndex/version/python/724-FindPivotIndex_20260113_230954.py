# Last updated: 1/13/2026, 11:09:54 PM
# first do sum of all array store it in left now start from i = 0 subtract the nums[i] from left then then check if left == right if not add the that nums[i] to right
1class Solution(object):
2    def pivotIndex(self, nums):
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