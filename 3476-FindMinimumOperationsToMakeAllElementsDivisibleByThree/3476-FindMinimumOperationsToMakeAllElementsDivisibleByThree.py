# Last updated: 12/10/2025, 8:21:02 AM
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            while nums[i] % 3 != 0:
                if (nums[i]+1) % 3 == 0:
                    nums[i]+=1
                    c+=1
                else:
                    nums[i]-=1
                    c+=1
        return c
        