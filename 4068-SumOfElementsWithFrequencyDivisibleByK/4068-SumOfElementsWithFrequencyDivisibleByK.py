# Last updated: 12/10/2025, 8:20:43 AM
class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = {}
        sum = 0
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i]+=1

        for key in h:
            if h[key]%k==0:
                sum+=h[key]*key
        return sum
            
        
        