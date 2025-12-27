# Last updated: 12/27/2025, 8:22:57 PM
1class Solution(object):
2    def buildArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        ans = []
8        for i in range(len(nums)):
9            ans.append(nums[nums[i]])
10        return ans
11        