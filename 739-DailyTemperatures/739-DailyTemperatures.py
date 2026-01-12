# Last updated: 1/12/2026, 11:25:45 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        s = [0]
        
        ans = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            while s!= [] and temperatures[i]>temperatures[s[-1]]:
                ans[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        while s!=[]:
            ans[s[-1]] = 0
            s.pop()
        return ans

        
        