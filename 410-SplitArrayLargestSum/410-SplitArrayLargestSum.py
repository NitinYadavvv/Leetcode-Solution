# Last updated: 2/26/2026, 7:48:22 AM
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def helper(mid):
            ans = 0
            sum = 0
            for i in nums:
                if sum+i>mid:
                    sum = 0
                    ans+=1
                sum+=i
            if sum != 0:
                ans+=1
            return ans<=k

        
        low = max(nums)
        high = sum(nums)
        while low<=high:

            mid = low + (high-low)//2

            if helper(mid):
                high = mid-1
            else:
                low = mid+1
        return low