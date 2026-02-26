# Last updated: 2/26/2026, 7:48:04 AM
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        def helper(cap):
            ans = 1
            sum = 0
            i = 0
            while i<len(weights):
                if sum+weights[i]>cap:
                    ans+=1
                    sum=0
                sum+=weights[i]
                i+=1
            return ans<=days



        low = max(weights)
        high = sum(weights)

        while low<=high:
            mid = low + (high-low)//2

            if helper(mid):
                high = mid-1
            else:
                low = mid+1
        return low