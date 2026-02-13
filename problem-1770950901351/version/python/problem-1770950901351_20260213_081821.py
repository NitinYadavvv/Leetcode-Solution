# Last updated: 2/13/2026, 8:18:21 AM
# try bruteforce convert each letter check in the dictionary maintain the level also
1from collections import deque
2class Solution:
3    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
4
5        q = deque([[beginWord,1]])
6        s = set(wordList)
7        
8        if endWord not in wordList:
9            return 0
10
11        while q:
12            word , level = q.popleft()
13            level+=1
14            for i in range(len(word)):
15
16                for j in 'abcdefghijklmnopqrstuvwxyz':
17                    new = word[:i]+j+word[i+1:]
18                    if new == endWord:
19                        return level
20                    if new in s and new!=word:
21                        q.append([new,level])
22                        s.remove(new)
23        return 0
24        