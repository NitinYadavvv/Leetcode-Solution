# Last updated: 12/16/2025, 10:35:48 AM
class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        Lsum = 0
        Ssum = 0
        last = -1
        for i in range(k):
            Ssum += nums[i]
            Lsum += nums[last]
            last -= 1

        return abs(Lsum - Ssum)