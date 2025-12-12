# Last updated: 12/12/2025, 9:04:50 PM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = set()
        for i in nums:
            if i in h:
                return True
            else:
                h.add(i)
        return False