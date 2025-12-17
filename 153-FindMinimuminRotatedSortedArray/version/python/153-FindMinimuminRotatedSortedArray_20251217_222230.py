# Last updated: 12/17/2025, 10:22:30 PM
# MY only goal to solve this question is to find the deflection if i find out from where the array is roated then i can easily find my answer so at first i just found normal  mid after finding the middle element i compare it to the first element here i can only get two cases whether my mid element is in left part of the deflection or the right part if its in left part then i will check whether my mid element is deflection or not by checking the next element if not then move low to mid + 1 and mid is in right part then end = mid -1 and also if array is not roated then first i will check that if my first element is greater then or not from my last element
1class Solution(object):
2    def findMin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        low = 0
8        end = len(nums)-1
9        first = nums[0]
10        
11        if first <= nums[end]:
12            return first
13
14        while low<=end:
15            mid = (low + end)//2
16            if nums[mid]>=first:
17                if nums[mid]>nums[mid+1]:
18                    return nums[mid+1]
19                low = mid+1
20            elif nums[mid] > nums[mid-1]:
21                end = mid-1
22            else:
23                return nums[mid]
24
25