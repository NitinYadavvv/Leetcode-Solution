# Last updated: 2/20/2026, 6:51:23 AM
# use binary search and take a look at koko bananans
1class Solution(object):
2    def splitArray(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8
9        def helper(mid):
10            ans = 0
11            sum = 0
12            for i in nums:
13                if sum+i>mid:
14                    sum = 0
15                    ans+=1
16                sum+=i
17            if sum != 0:
18                ans+=1
19            return ans<=k
20
21        
22        low = max(nums)
23        high = sum(nums)
24        while low<=high:
25
26            mid = low + (high-low)//2
27
28            if helper(mid):
29                high = mid-1
30            else:
31                low = mid+1
32        return low