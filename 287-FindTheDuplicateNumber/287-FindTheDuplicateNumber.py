# Last updated: 12/10/2025, 8:21:58 AM
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = nums
        l.sort()
        i = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                return nums[i]
            i+=1
        