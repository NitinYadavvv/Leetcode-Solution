# Last updated: 2/12/2026, 10:51:26 PM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums[0] = 0
        nums.sort()
        return ans + nums[1]+nums[2]
       