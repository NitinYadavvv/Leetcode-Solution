# Last updated: 12/10/2025, 8:22:00 AM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """ 
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)