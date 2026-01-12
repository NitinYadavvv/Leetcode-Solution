# Last updated: 1/12/2026, 11:25:42 PM
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def helper(k):
            sum = 0
            for i in piles:
               sum += (i+k-1)//k
            if sum > h:
                return False
            return True

        
        high = max(piles)
        low = 1
        
        while low<=high:
            mid = low+ (high - low)//2
            if helper(mid):
                high = mid-1
            else:
                low = mid+1
        return low


        