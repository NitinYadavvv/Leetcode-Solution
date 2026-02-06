# Last updated: 2/6/2026, 9:19:07 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        ans = set(range(1,len(nums)+1))
4        for i in nums:
5            ans.discard(i)
6        return list(ans)
7        