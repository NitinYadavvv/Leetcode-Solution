# Last updated: 2/19/2026, 8:17:58 AM
# binary search koko eats bananan
1class Solution(object):
2    def shipWithinDays(self, weights, days):
3        """
4        :type weights: List[int]
5        :type days: int
6        :rtype: int
7        """
8
9        def helper(cap):
10            ans = 1
11            sum = 0
12            i = 0
13            while i<len(weights):
14                if sum+weights[i]>cap:
15                    ans+=1
16                    sum=0
17                sum+=weights[i]
18                i+=1
19            return ans<=days
20
21
22
23        low = max(weights)
24        high = sum(weights)
25
26        while low<=high:
27            mid = low + (high-low)//2
28
29            if helper(mid):
30                high = mid-1
31            else:
32                low = mid+1
33        return low