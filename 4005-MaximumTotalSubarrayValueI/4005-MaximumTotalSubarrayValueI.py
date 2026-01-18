# Last updated: 1/18/2026, 6:17:30 PM
class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return (max(nums)-min(nums))*k
        