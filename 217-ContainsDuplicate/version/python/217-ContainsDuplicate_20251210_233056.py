# Last updated: 12/10/2025, 11:30:56 PM
# Use this using set if the value already in the set it mean it appear twice
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        h = set()
8        for i in nums:
9            if i in h:
10                return True
11            else:
12                h.add(i)
13        return False