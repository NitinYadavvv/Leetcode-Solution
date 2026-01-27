# Last updated: 1/27/2026, 5:41:38 PM
# use BFS or DFS
1from collections import deque
2class Solution:
3    def numIslands(self, grid: List[List[str]]) -> int:
4        
5
6        def bfs(i,j):
7            q = deque([[i,j]])
8            grid[i][j] = '0'
9            while q:
10                k,l = q.popleft()
11                
12                check = [[0,1],[1,0],[-1,0],[0,-1]]
13                for c in check:
14                    nk = k+c[0]
15                    nl = l+c[1]
16
17                    if nk>=0 and nl>=0 and nk<len(grid) and nl<len(grid[0]):
18                        if grid[nk][nl] == '1':
19                            grid[nk][nl] = '0'
20                            q.append([nk,nl])
21                                        
22        ans = 0
23        for i in range(len(grid)):
24            for j in range(len(grid[0])):
25                if grid[i][j] == '1':
26                    bfs(i,j)
27                    ans+=1
28        return ans  
29
30