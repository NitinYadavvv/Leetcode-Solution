# Last updated: 12/10/2025, 8:22:20 AM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = float('inf')
        j = 0
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>= target:
                res = min(i-j+1,res)
                sum -= nums[j]
                j+=1
            
        return 0 if res == float('inf') else res

            
        