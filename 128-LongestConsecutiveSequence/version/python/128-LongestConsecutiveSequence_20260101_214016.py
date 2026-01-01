# Last updated: 1/1/2026, 9:40:16 PM
# so first of all we will create a set of our array once it created it will delete the duplicated then pick the value in the set one by one if the value - 1 is present in the set thats mean this is not the starting point of the sequence when we encounter the value -1 and if that is not present in set mean this is the possible starting point of the maximum sequence then we check till we find the value +1 in the set and calculate the longest length
1class Solution(object):
2    def longestConsecutive(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        s = set(nums)
8        ans = 0
9        for i in s:
10            if i-1 not in s:
11                l = 1
12                x = i
13                while x+1 in s:
14                    x+=1
15                    l+=1
16                ans = max(l,ans)
17        return ans