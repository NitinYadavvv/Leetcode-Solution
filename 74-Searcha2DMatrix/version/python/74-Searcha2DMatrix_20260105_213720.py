# Last updated: 1/5/2026, 9:37:20 PM
# kind of binary search but not fully a binary search here we dont calculate medium instead of that we will start from the top right corner that is m[0][len(matrix[0]]  and check if the its equal to target if not then greater then target its me it wil greater then all the coloumn below it so we decrese column by 1 and if its smaller then target we will increase row by 1
1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        
9
10        r = 0 
11        c = len(matrix[0])-1
12        
13        while r<len(matrix) and c>=0:
14
15            if matrix[r][c] == target:
16                return True
17            elif matrix[r][c] > target:
18                c-=1
19            else:
20                r+=1
21        return False
22            