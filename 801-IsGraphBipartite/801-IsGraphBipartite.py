# Last updated: 2/26/2026, 7:48:11 AM
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        visit = [-1]*len(graph)
        def helper(node,color):
            if visit[node] != -1:
                if visit[node]!=color:
                    return False
                return True

            visit[node] = color
            
            for i in graph[node]:
                if color == 'R':
                    if not helper(i,'G'):
                        return False
                elif color == 'G':
                    if not helper(i,'R'):
                        return False
            return True

        for i in range(len(visit)):
            if visit[i] == -1:
                if not helper(i,'R'):
                    return False
        return True