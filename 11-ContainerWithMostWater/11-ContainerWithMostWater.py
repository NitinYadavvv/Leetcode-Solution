# Last updated: 12/10/2025, 8:25:00 AM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        res = 0
        while i!=j and j>i:
            if height[i]<height[j]:
                ans = height[i] * (j-i)
                i+=1
            elif height[i]>height[j]:
                ans = height[j] * (j-i)
                j-=1
            else:
                ans = height[i] * (j-i)
                i+=1
                j-=1
            if ans>res:
                res= ans
        return res





        