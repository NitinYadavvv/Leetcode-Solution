# Last updated: 1/12/2026, 11:26:42 PM
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        end = len(nums)-1
        first = nums[0]
        
        if first <= nums[end]:
            return first

        while low<=end:
            mid = (low + end)//2
            if nums[mid]>=first:
                if nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                low = mid+1
            elif nums[mid] > nums[mid-1]:
                end = mid-1
            else:
                return nums[mid]

