# Last updated: 12/10/2025, 8:20:58 AM
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h = {}
        res = []
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                res.append(i)
        return res