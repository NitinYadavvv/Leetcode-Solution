# Last updated: 2/12/2026, 10:51:42 PM
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        for i in range(len(nums)//2):
            var = nums[i]+nums[len(nums)-i-1]
            m = max(m,var)
        return m
        