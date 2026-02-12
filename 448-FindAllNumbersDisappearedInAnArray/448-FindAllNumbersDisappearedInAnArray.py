# Last updated: 2/12/2026, 10:52:14 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set(range(1,len(nums)+1))
        for i in nums:
            ans.discard(i)
        return list(ans)
        