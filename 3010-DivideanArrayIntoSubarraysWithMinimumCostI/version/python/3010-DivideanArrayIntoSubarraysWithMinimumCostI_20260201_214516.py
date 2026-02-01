# Last updated: 2/1/2026, 9:45:16 PM
# first element is fixed other two are minimum of rest the array
1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        ans = nums[0]
4        nums[0] = 0
5        nums.sort()
6        return ans + nums[1]+nums[2]
7       