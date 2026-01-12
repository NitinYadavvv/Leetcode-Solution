# Last updated: 1/12/2026, 11:25:05 PM
class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        ans = 0
        arr = []

        for i in range(len(nums)): 

            for j in range(i,len(nums)): 
                arr = nums[i:j+1]
                s = sum(nums[i:j+1]) 
                if s in arr:
                    ans +=1         
        return ans
        
        