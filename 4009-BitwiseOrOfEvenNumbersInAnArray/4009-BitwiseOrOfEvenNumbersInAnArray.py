# Last updated: 1/18/2026, 6:17:27 PM
class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
               ans = ans | nums[i]
        return ans
        