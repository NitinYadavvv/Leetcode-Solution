# Last updated: 12/10/2025, 8:22:17 AM
from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """  
        self.q1.append(x)
    def pop(self):
        """
        :rtype: int
        """
        while len(self.q1)!=1:
            self.q2.append(self.q1.popleft())
        a = self.q1.popleft()        
        while self.q2:
            self.q1.append(self.q2.popleft())
        return a
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()