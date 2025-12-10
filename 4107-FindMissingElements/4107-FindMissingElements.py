# Last updated: 12/10/2025, 8:20:42 AM
class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        j = 0
        for i in range(1,len(nums)):
            r = nums[i]-nums[i-1]
            for j in range(1,r):
                res.append(nums[i-1]+j)

        return res
            
            
        