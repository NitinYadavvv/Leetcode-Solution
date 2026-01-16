# Last updated: 1/16/2026, 10:20:22 PM
# Easy
1class Solution(object):
2    def evenNumberBitwiseORs(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        ans = 0
8        for i in range(len(nums)):
9            if nums[i] % 2 == 0:
10               ans = ans | nums[i]
11        return ans
12        