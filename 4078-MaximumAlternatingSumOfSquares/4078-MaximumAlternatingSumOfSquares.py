# Last updated: 12/10/2025, 8:20:48 AM
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        for i in nums:
            new.append(abs(i))
        new.sort()
        j = len(new)-1
        res = 0
        i = 0
        while i<j:
            res+=new[j]**2-new[i]**2
            j-=1
            i+=1
        if i == j:
            res+=new[j]**2
        return res
            
            
            
        