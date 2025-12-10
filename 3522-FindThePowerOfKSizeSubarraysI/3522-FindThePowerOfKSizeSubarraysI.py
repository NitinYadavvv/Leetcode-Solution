# Last updated: 12/10/2025, 8:21:00 AM
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = [-1] * (len(nums) - k+1)
        c = 1
        for i in range(1,k):
            if nums[i]==nums[i-1]+1:
                c+=1
            else:
                c=1
        if c==k:
            l[0] = nums[k-1]
        
        i = 1
        for j in range(k,len(nums)):
            if nums[j] == nums[j-1]+1:
                c+=1
            else:
                c = 1
            if c>=k:
                l[i] = nums[j]  
            i+=1
        return l


                

            

