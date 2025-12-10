# Last updated: 12/10/2025, 8:24:54 AM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        for i in range(len(nums)):
            h={}
            for j in range(i+1,len(nums)):
                k = -(nums[i]+nums[j])
                if k in h:
                    l = [nums[i],nums[j],k]
                    l.sort()
                    res.add((tuple(l)))
                h[nums[j]] = j
        return list(res)
                    
