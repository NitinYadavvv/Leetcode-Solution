# Last updated: 12/10/2025, 8:21:24 AM
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            l.append(s)
        return l