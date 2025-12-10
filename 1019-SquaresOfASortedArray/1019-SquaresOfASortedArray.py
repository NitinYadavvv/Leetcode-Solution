# Last updated: 12/10/2025, 8:21:33 AM
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0 
        j = len(nums)-1
        l = [] 
        while j>=i:
            if nums[i]**2 > nums[j]**2:
               l.append(nums[i]**2)
               i+=1
            else:
                l.append(nums[j]**2)
                j-=1
            
        return l[::-1]

        