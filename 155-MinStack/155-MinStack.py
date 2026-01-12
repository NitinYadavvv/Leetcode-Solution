# Last updated: 1/12/2026, 11:26:40 PM
class MinStack(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.min = None

    def push(self, val):
        if not self.s1:
            self.min = val
        elif val <= self.min:
            self.s2.append(self.min)
            self.min = val
        self.s1.append(val)

    def pop(self):
        if self.s1[-1] == self.min:
            self.min = self.s2.pop() if self.s2 else None
        self.s1.pop()

    def top(self):
        return self.s1[-1]

    def getMin(self):
        return self.min
