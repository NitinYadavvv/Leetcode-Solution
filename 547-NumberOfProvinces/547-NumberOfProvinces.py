# Last updated: 2/12/2026, 10:52:11 PM
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)-1
        visit = [0]*(n+1)
        source = 0
        q = deque()    
        ans = 0
        
        for city in range(len(visit)):
            if visit[city] == 0:
                q.append(city)
                ans+=1
                while q:
                    node = q.popleft()
                    for i in range(len(isConnected[node])):
                        if isConnected[node][i] == 1 and visit[i]==0:
                            visit[i] = 1
                            q.append(i) 
        return ans               


                

        