# Last updated: 12/14/2025, 8:10:18 AM
# sort the array then run a loop get first K and last K element then find abs diffrence
1class Solution(object):
2    def absDifference(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        nums.sort()
9        Lsum = 0
10        Ssum = 0
11        last = -1
12        for i in range(k):
13            Ssum += nums[i]
14            Lsum += nums[last]
15            last -= 1
16
17        return abs(Lsum - Ssum)