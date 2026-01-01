# Last updated: 1/1/2026, 11:22:50 PM
# one pointer at end and one at start if sum of both is larger then target then decrement end pointer if not then increment start pointer until both sum reaches to target
1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        first = 0
9        last = len(numbers)-1
10        while (numbers[first]+numbers[last]) != target:
11            if (numbers[first]+numbers[last]) > target:
12                last -=1
13            else:
14                first+=1
15        return [first+1,last+1]
16        