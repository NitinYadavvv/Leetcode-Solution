# Last updated: 12/10/2025, 8:22:35 AM
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        o = len(nums)
        k = k%o
        nums[:] =  nums[-k:]+nums[:-k]

