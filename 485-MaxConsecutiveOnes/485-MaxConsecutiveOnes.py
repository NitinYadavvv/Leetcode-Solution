# Last updated: 12/10/2025, 8:21:48 AM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        j = 0
        for j in range(len(nums)):

            if nums[j]==0:
                ans = max(j-i,ans)
                i = j+1
        ans = max(len(nums)-i,ans)
        return ans