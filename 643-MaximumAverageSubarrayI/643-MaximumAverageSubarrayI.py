# Last updated: 12/10/2025, 8:21:42 AM
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        res = s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            if s>res:
                res = s
        return res/float(k)
        



        