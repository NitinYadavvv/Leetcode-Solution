# Last updated: 2/12/2026, 10:52:06 PM
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def bfs(i,j):
            q = deque([[i,j]])
            grid[i][j] = 0
            count = 1

            while q:
                k , l = q.popleft()
                check  = [[0,1],[1,0],[-1,0],[0,-1]]
                for c in check:
                    nk = c[0]+k
                    nl = c[1]+l

                    if nk>=0 and nl>=0 and nk<len(grid) and nl<len(grid[0]):
                        if grid[nk][nl] == 1:
                            q.append([nk,nl])
                            grid[nk][nl] = 0
                            count+=1
            return count

        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    val = bfs(i,j)
                    ans = max(val,ans)
        return ans