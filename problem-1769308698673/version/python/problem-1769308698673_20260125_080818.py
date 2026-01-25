# Last updated: 1/25/2026, 8:08:18 AM
1class Solution:
2    def minimumPrefixLength(self, nums: List[int]) -> int:
3        i = 0 
4        j = 0 
5        while j<len(nums)-1:
6            if nums[j+1]>nums[j]:
7                j+=1
8            else:
9                j+=1
10                i = j
11        return i