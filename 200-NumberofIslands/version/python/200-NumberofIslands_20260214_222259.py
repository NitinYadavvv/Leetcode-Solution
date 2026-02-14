# Last updated: 2/14/2026, 10:22:59 PM
# fill each other not with R or G use DFS
1class Solution:
2    def isBipartite(self, graph: List[List[int]]) -> bool:
3        
4        visit = [-1]*len(graph)
5        def helper(node,color):
6            if visit[node] != -1:
7                if visit[node]!=color:
8                    return False
9                return True
10
11            visit[node] = color
12            
13            for i in graph[node]:
14                if color == 'R':
15                    if not helper(i,'G'):
16                        return False
17                elif color == 'G':
18                    if not helper(i,'R'):
19                        return False
20            return True
21
22        for i in range(len(visit)):
23            if visit[i] == -1:
24                if not helper(i,'R'):
25                    return False
26        return True