# Last updated: 1/24/2026, 7:02:45 AM
# its kinda sort of the question
1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        nums.sort()
4        m = 0
5        for i in range(len(nums)//2):
6            var = nums[i]+nums[len(nums)-i-1]
7            m = max(m,var)
8        return m
9        