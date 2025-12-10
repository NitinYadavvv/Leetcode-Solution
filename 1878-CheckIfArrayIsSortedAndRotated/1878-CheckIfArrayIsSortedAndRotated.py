# Last updated: 12/10/2025, 8:21:20 AM
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0 
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                c+=1
        if nums[0]<nums[len(nums)-1]:
            c+=1
        if c==0 or c==1:
            return True
        return False