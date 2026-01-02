# Last updated: 1/2/2026, 11:19:29 PM
# its a simple fixed size sliding window problem where we fixed are window len with s1 length and take hashmap of each window and compare that hashmap with s1 's hashmap if its matchs we found are answer
1class Solution(object):
2    def checkInclusion(self, s1, s2):
3        """
4        :type s1: str
5        :type s2: str
6        :rtype: bool
7        """
8        h = {}
9        for ch in s1:
10            if ch in h:
11                h[ch]+=1
12            else:
13                h[ch]=1
14        i = 0
15        j = len(s1)-1
16        while j<len(s2):
17            h1 = {}
18            k = i
19            while k<=j:
20                if s2[k] not in h1:
21                    h1[s2[k]] = 1
22                else:
23                    h1[s2[k]]+=1
24                k+=1
25            if h1 == h:
26                return True
27            i+=1
28            j+=1
29        return False
30        
31
32
33
34
35
36        