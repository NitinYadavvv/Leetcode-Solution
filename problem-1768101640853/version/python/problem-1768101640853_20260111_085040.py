# Last updated: 1/11/2026, 8:50:40 AM
1class Solution(object):
2    def centeredSubarrays(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if len(nums) == 1:
8            return 1
9        ans = 0
10        arr = []
11
12        for i in range(len(nums)): 
13
14            for j in range(i,len(nums)): 
15                arr = nums[i:j+1]
16                s = sum(nums[i:j+1]) 
17                if s in arr:
18                    ans +=1         
19        return ans
20        
21        