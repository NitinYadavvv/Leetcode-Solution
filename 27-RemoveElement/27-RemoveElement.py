# Last updated: 12/10/2025, 8:24:43 AM
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """ 
        i = 0
        j = len(nums)
        while i<j:
            if nums[i] == val:
                nums.remove(nums[i])
                j-=1
            else:
                i+=1
        return len(nums)
          
