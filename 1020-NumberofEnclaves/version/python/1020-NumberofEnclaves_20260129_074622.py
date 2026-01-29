# Last updated: 1/29/2026, 7:46:22 AM
# do BFS or DFS only on boundaries 1s then scan again if any 1s left count them that's your answer
1from collections import deque
2class Solution:
3    def numEnclaves(self, grid: List[List[int]]) -> int:
4
5
6        def bfs(i,j):
7            q = deque([[i,j]])
8            grid[i][j] = 0
9            check = [[0,1],[1,0],[-1,0],[0,-1]]
10            while q:
11                i,j = q.popleft()
12                for c in check:
13                    ni = c[0]+i
14                    nj = c[1]+j
15                    if ni>=0 and nj>=0 and ni<len(grid) and nj<len(grid[0]):
16                        if grid[ni][nj] == 1:
17                            q.append([ni,nj])
18                            grid[ni][nj] = 0
19            
20        for i in range(len(grid)):
21            for j in range(len(grid[0])):
22                if grid[i][j] == 1:
23                    if i==0 or i == len(grid)-1 or j == 0 or j==len(grid[0])-1:
24                        bfs(i,j)
25        ans = 0
26        for i in range(len(grid)):
27            for j in range(len(grid[0])):
28                if grid[i][j] == 1:
29                    ans+=1
30        return ans