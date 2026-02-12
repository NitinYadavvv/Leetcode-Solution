# Last updated: 2/12/2026, 10:51:54 PM
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 2:
                        q.append([i,j])
                    elif grid[i][j] == 1:
                        fresh+=1
        
        if fresh == 0:
            return 0
        min = 0
        copy = grid
        while q and fresh>0:
            
            l = len(q)
            min +=1
            for _ in range(l):
                i,j = q.popleft()
                check = [[0,1],[1,0],[-1,0],[0,-1]]
                for k,o in check:
                    ni=i+k
                    nj=j+o
                    if ni<0 or nj<0 or ni>=len(copy) or nj>=len(copy[0]):
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh-=1
                        q.append([ni,nj])
        if fresh>0:
            return -1
        return min




