# Last updated: 1/18/2026, 6:19:52 PM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        n = len(nums)
        j = 0
        i = 0
        while i<len(nums):
            j = i+1
            while len(nums)>j and nums[j]==nums[i]:
                j+=1
            if (j-i) > n//3:
                res.append(nums[i])
            i = j
        return res
            
