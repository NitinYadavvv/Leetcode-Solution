# Last updated: 12/10/2025, 8:21:03 AM
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 1
            else:
                hash[nums[i]]+=1
        m = max(hash.values())
        s = 0
        for v in hash.values():
            if v==m:
                s+=v
        return s
        