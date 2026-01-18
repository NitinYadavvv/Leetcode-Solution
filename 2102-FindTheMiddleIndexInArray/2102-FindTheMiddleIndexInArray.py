# Last updated: 1/18/2026, 6:18:01 PM
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0

        left = sum(nums)    
        for i in range(len(nums)):
         
            left-=nums[i]
            if left == right:
                return i
            right+=nums[i]

        return -1
        