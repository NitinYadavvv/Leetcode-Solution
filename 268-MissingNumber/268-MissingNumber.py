# Last updated: 12/10/2025, 8:22:01 AM
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[len(nums)-1] == len(nums):
            for i in range(len(nums)):
                if nums[i] != i:
                    return i
        return len(nums)
        
        