# Last updated: 12/10/2025, 8:24:09 AM
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        m = max(nums)+1
        count = [0] * m
        while len(nums)>0:
            num = nums.pop(0)
            count[num]+=1
        for i in range(len(count)):
            while count[i] > 0:
                nums.append(i)
                count[i]-=1
            
            



        
































































