# Last updated: 12/10/2025, 8:21:19 AM
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = nums
        for i in range(len(nums)):
            res.append(nums[i])
        return res