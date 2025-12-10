# Last updated: 12/10/2025, 8:21:21 AM
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = 0
        max = 0
        for i in range(len(accounts)):
            sum = 0 
            for j in range(len(accounts[i])):
                sum+=accounts[i][j]
            if(sum>=max):
                max = sum
        return max 




        