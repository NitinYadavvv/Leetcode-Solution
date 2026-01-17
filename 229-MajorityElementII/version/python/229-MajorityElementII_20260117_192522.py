# Last updated: 1/17/2026, 7:25:22 PM
# sort the array then add two pointer
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        nums.sort()
8        res = []
9        n = len(nums)
10        j = 0
11        i = 0
12        while i<len(nums):
13            j = i+1
14            while len(nums)>j and nums[j]==nums[i]:
15                j+=1
16            if (j-i) > n//3:
17                res.append(nums[i])
18            i = j
19        return res
20            
21