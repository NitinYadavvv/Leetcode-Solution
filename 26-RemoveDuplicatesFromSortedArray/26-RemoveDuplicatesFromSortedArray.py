# Last updated: 12/10/2025, 8:24:47 AM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        j = len(nums)-1
        while i<j:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
                j-=1
            else:
                i+=1
        return len(nums)    
           
        