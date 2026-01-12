# Last updated: 1/12/2026, 11:25:25 PM
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        