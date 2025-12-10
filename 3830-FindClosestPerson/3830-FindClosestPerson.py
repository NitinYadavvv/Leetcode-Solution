# Last updated: 12/10/2025, 8:20:54 AM
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        if abs(z-x) > abs(z-y):
            return 2
        if abs(z-x)< abs(z-y):
            return 1
        return 0 
        