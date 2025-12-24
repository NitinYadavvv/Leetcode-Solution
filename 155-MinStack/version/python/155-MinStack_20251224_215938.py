# Last updated: 12/24/2025, 9:59:38 PM
1class MinStack(object):
2
3    def __init__(self):
4        self.s1 = []
5        self.s2 = []
6        self.min = None
7
8    def push(self, val):
9        if not self.s1:
10            self.min = val
11        elif val <= self.min:
12            self.s2.append(self.min)
13            self.min = val
14        self.s1.append(val)
15
16    def pop(self):
17        if self.s1[-1] == self.min:
18            self.min = self.s2.pop() if self.s2 else None
19        self.s1.pop()
20
21    def top(self):
22        return self.s1[-1]
23
24    def getMin(self):
25        return self.min
26