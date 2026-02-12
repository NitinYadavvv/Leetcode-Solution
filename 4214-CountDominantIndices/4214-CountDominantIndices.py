# Last updated: 2/12/2026, 10:51:05 PM
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        domi = 0
        for i in range(len(nums)-1):
            if nums[i] > sum(nums[i+1:])/len(nums[i+1:]):
                domi+=1
        return domi
            
        