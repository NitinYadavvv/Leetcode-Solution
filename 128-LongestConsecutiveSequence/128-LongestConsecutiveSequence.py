# Last updated: 1/12/2026, 11:26:52 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = 0
        for i in s:
            if i-1 not in s:
                l = 1
                x = i
                while x+1 in s:
                    x+=1
                    l+=1
                ans = max(l,ans)
        return ans