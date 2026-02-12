# Last updated: 2/12/2026, 10:51:03 PM
class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        i = 0 
        j = 0 
        while j<len(nums)-1:
            if nums[j+1]>nums[j]:
                j+=1
            else:
                j+=1
                i = j
        return i