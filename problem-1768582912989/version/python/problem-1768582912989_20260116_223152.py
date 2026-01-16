# Last updated: 1/16/2026, 10:31:52 PM
# so simple just think about where i find my optimal answer its always in a window where my max and min of nums lies and how many window i will take from there k? and at that time my max and min will remain same its mean......
1class Solution(object):
2    def maxTotalValue(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        return (max(nums)-min(nums))*k
9        