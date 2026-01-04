# Last updated: 1/4/2026, 9:44:14 PM
1class Solution(object):
2    def dailyTemperatures(self, temperatures):
3        """
4        :type temperatures: List[int]
5        :rtype: List[int]
6        """
7        s = [0]
8        
9        ans = [0]*len(temperatures)
10        
11        for i in range(len(temperatures)):
12            while s!= [] and temperatures[i]>temperatures[s[-1]]:
13                ans[s[-1]] = i - s[-1]
14                s.pop()
15            s.append(i)
16        while s!=[]:
17            ans[s[-1]] = 0
18            s.pop()
19        return ans
20
21        
22        