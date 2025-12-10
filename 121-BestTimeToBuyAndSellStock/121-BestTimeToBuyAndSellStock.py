# Last updated: 12/10/2025, 8:22:53 AM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = 0
        chep = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<chep:
                chep = prices[i]
            elif prices[i]-chep > pro:
                pro = prices[i]-chep
        return pro

                
        return pro


          

            
