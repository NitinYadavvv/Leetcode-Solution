# Last updated: 1/18/2026, 6:21:47 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        l = 0
        h = len(matrix)*len(matrix[0])-1

        while l<=h:
            mid = (l+h)//2

            r = mid//len(matrix[0])
            c = mid % len(matrix[0])

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = mid+1
            else:
                h = mid-1
        return False            
                