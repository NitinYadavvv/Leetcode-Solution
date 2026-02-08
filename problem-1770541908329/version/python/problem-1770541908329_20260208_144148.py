# Last updated: 2/8/2026, 2:41:48 PM
1class Solution:
2    def dominantIndices(self, nums: List[int]) -> int:
3        domi = 0
4        for i in range(len(nums)-1):
5            if nums[i] > sum(nums[i+1:])/len(nums[i+1:]):
6                domi+=1
7        return domi
8            
9        