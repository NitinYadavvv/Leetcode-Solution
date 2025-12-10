# Last updated: 12/10/2025, 8:20:53 AM
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum(nums) % k


        