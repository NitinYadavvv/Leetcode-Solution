# Last updated: 1/8/2026, 8:19:29 PM
'''
so in this we use a binary search on a range of 1 - max per hour speed to eat all banana 

so max speed is the maximum element in the array so we do a range of 1 - to max element then apply binary search on that and do one extra helper to calculate the mid is suffiencent
'''

1class Solution(object):
2    def minEatingSpeed(self, piles, h):
3        """
4        :type piles: List[int]
5        :type h: int
6        :rtype: int
7        """
8
9        def helper(k):
10            sum = 0
11            for i in piles:
12               sum += (i+k-1)//k
13            if sum > h:
14                return False
15            return True
16
17        
18        high = max(piles)
19        low = 1
20        
21        while low<=high:
22            mid = low+ (high - low)//2
23            if helper(mid):
24                high = mid-1
25            else:
26                low = mid+1
27        return low
28
29
30        