# Last updated: 12/10/2025, 8:21:28 AM
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            if len(nums[i])%2==0:
                ans+=1
        return ans