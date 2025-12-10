# Last updated: 12/10/2025, 8:21:41 AM
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0


        res = 0
        pro = 1
        j = 0
        i = 0

        while j<len(nums):
            pro*=nums[j]
            while pro >= k:
                pro /= nums[i]
                i += 1
            res += (j - i + 1)
            j+=1
        
        return res
            
        