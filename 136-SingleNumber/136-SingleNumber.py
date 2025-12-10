# Last updated: 12/10/2025, 8:22:47 AM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash ={}
        c = 0
        for i in range(len(nums)):
           c = c ^ nums[i]
            
        return c

        




       
        