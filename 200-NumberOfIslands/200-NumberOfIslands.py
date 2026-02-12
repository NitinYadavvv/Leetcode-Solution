# Last updated: 2/12/2026, 10:52:41 PM
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def bfs(i,j):
            q = deque([[i,j]])
            grid[i][j] = '0'
            while q:
                k,l = q.popleft()
                
                check = [[0,1],[1,0],[-1,0],[0,-1]]
                for c in check:
                    nk = k+c[0]
                    nl = l+c[1]

                    if nk>=0 and nl>=0 and nk<len(grid) and nl<len(grid[0]):
                        if grid[nk][nl] == '1':
                            grid[nk][nl] = '0'
                            q.append([nk,nl])
                                        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i,j)
                    ans+=1
        return ans  

