# Last updated: 12/10/2025, 8:24:38 AM
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = 0
        e = len(nums)-1
        while(s<=e):
            mid = s + (e-s)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                e = mid-1
            else:
                s = mid+1
        if s>e:
            return s
        else:
            return e
        