# Last updated: 12/16/2025, 10:36:38 AM
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        
        left = 1
        for i in range(len(nums)):
            res[i]*=left
            left*=nums[i]
        
        right = 1
        for i in range(len(res)-1,-1,-1):
            res[i] *= right
            right  *= nums[i]
        return res



        
            
        