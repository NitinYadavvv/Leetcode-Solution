# Last updated: 1/12/2026, 11:26:38 PM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        last = len(numbers)-1
        while (numbers[first]+numbers[last]) != target:
            if (numbers[first]+numbers[last]) > target:
                last -=1
            else:
                first+=1
        return [first+1,last+1]
        