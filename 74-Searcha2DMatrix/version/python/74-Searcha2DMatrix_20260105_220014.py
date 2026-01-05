# Last updated: 1/5/2026, 10:00:14 PM
'''
treat this same as binary search problem take low as 0 and high as m*n-1 then calculate the medium now the big task it how to convert the medium to 2d  so there are two formula 

for row = mid // len of column (len(matrix[0])
for column = mid % len of column (len(matrix[0])

this will give the coordinate then we can easlily check == , < , > then target and set low and high
'''

1class Solution(object):
2    def searchMatrix(self, matrix, target):
3        """
4        :type matrix: List[List[int]]
5        :type target: int
6        :rtype: bool
7        """
8        
9        l = 0
10        h = len(matrix)*len(matrix[0])-1
11
12        while l<=h:
13            mid = (l+h)//2
14
15            r = mid//len(matrix[0])
16            c = mid % len(matrix[0])
17
18            if matrix[r][c] == target:
19                return True
20            elif matrix[r][c] < target:
21                l = mid+1
22            else:
23                h = mid-1
24        return False            
25                