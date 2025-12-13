# Last updated: 12/13/2025, 11:57:28 PM
# first calculate left by using another array then traverse it from reverse while multipy it by right value
1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        res = [1]*len(nums)
8        
9        left = 1
10        for i in range(len(nums)):
11            res[i]*=left
12            left*=nums[i]
13        
14        right = 1
15        for i in range(len(res)-1,-1,-1):
16            res[i] *= right
17            right  *= nums[i]
18        return res
19
20
21
22        
23            
24        