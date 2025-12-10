# Last updated: 12/10/2025, 8:21:13 AM
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if nums[i] == original:
                original*=2
                i = 0
            else:
                i+=1
        return original
        