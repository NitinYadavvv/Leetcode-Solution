# Last updated: 2/12/2026, 10:51:53 PM
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:


        def bfs(i,j):
            q = deque([[i,j]])
            grid[i][j] = 0
            check = [[0,1],[1,0],[-1,0],[0,-1]]
            while q:
                i,j = q.popleft()
                for c in check:
                    ni = c[0]+i
                    nj = c[1]+j
                    if ni>=0 and nj>=0 and ni<len(grid) and nj<len(grid[0]):
                        if grid[ni][nj] == 1:
                            q.append([ni,nj])
                            grid[ni][nj] = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i==0 or i == len(grid)-1 or j == 0 or j==len(grid[0])-1:
                        bfs(i,j)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans+=1
        return ans