# Last updated: 12/11/2025, 11:48:49 AM
# in hashing use tuple to store the value cause hashing does not support list thats why first sort the particular string then make a key of it and if that key already present in hash map just add the string to that key in end just return the list of all value of hashmap
1class Solution(object):
2    def groupAnagrams(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: List[List[str]]
6        """
7        h ={}
8        res = []
9        for i in strs:
10            s = tuple(sorted(i))
11            if s not in h:
12                h[s] = [i]
13            else:
14                h[s].append(i)
15        return list(h.values())
16
17
18
19
20    
21
22
23
24        