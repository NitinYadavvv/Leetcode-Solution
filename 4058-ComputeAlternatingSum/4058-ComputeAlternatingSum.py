# Last updated: 12/10/2025, 8:20:49 AM
class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum+=nums[i]
            else:
                sum -= nums[i]
        return sum
                
        