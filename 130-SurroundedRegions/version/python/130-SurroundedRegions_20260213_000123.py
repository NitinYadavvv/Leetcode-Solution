# Last updated: 2/13/2026, 12:01:23 AM
# instead of thinking about find the the O that surrounded by X found those Os who are touching border cause they will not gonna be the answer and also there neighbours so mark all them false then found the remainng Os who are not false and is a Os
1from collections import deque
2class Solution:
3    def solve(self, board: List[List[str]]) -> None:
4        """
5        Do not return anything, modify board in-place instead.
6        """
7        
8        def bfs(i,j):
9            q = deque([[i,j]])
10            while q:
11                var = q.popleft()
12                ni = var[0]
13                nj = var[1]
14                c = [[1,0],[0,1],[-1,0],[0,-1]]
15                for check in c:
16                    ni=var[0]+check[0]
17                    nj=var[1]+check[1]
18
19                    if ni>=0 and ni<len(board) and nj>=0 and nj<len(board[0]):
20                        if board[ni][nj] == 'O' and grid[ni][nj] == 0:
21                            q.append([ni,nj])
22                            grid[ni][nj] = 1
23            
24
25
26        m = len(board)
27        n = len(board[0])
28
29        grid = [[0] * n for _ in range(m)]
30        for i in range(len(board)):
31            for j in range(len(board[0])):
32                if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == 'O' and grid[i][j] ==0:
33                    grid[i][j] = 1
34                    bfs(i, j)
35
36        for i in range(m):
37            for j in range(n):
38                if grid[i][j] == 0 and board[i][j] == 'O':
39                    board[i][j] = 'X'
40    
41        