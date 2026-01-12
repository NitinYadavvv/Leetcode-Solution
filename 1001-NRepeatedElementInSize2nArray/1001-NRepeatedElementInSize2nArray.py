# Last updated: 1/12/2026, 11:25:39 PM
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i in h:
                return i
            h[i] = 1