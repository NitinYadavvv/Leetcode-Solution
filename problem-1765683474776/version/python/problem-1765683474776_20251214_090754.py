# Last updated: 12/14/2025, 9:07:54 AM
'''
make a list of that string first
first of all i count the number of vowels present in first word then start my index from the remaing words left
'''

1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        vow = ['a','e','i','o','u']
8        c = 0
9        s = list(s)
10        index = 0
11        for i in range(len(s)):
12            if s[i] == ' ':
13                index = i
14                break
15            if s[i] in vow:
16                c+=1
17
18        if index == 0:
19            return "".join(s)
20        i = index+1
21        
22        
23        while i<len(s):
24            j = i
25            count = 0
26            while i<len(s) and s[i] != ' ':
27                if s[i] in vow:
28                    count+=1
29                i+=1
30            e = i-1 
31            if count == c:
32                while j<e:
33                    s[e] , s[j] = s[j] , s[e]
34                    j+=1
35                    e-=1
36            i+=1
37        return "".join(s)                    
38        