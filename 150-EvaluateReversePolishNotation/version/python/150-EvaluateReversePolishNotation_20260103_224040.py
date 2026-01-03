# Last updated: 1/3/2026, 10:40:40 PM
# simple when you encounter the operator pop last 2 element and append thier result with that operator
1class Solution(object):
2    def evalRPN(self, tokens):
3        """
4        :type tokens: List[str]
5        :rtype: int
6        """
7        s = []
8
9        for i in tokens:
10            
11
12            if i == '+' or i == '-' or i == '*' or i =='/':
13                b = s.pop()
14                a = s.pop()
15
16                if i == '+':
17                    s.append(a+b)
18                elif i == '-':
19                    s.append(a-b)
20                elif i == '*':
21                    s.append(a*b)
22                elif i == '/':
23                    s.append(int(float(a)/b))
24            else:
25                s.append(int(i))
26
27        return s[-1]
28        