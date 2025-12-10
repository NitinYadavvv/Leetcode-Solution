# Last updated: 12/10/2025, 8:20:57 AM
class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1,len(nums)):
            ans = sum(nums[0:i]) - sum(nums[i:len(nums)])
            if ans % 2 == 0 or ans == 0:
                res+=1
        return res

        