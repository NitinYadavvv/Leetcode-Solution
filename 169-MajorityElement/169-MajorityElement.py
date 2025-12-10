# Last updated: 12/10/2025, 8:22:38 AM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        c = 0
        h={}
        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
                if h[i] > n:
                    return i
        return nums[0]
        
        