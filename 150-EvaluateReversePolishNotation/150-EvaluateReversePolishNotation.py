# Last updated: 1/12/2026, 11:26:44 PM
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []

        for i in tokens:
            

            if i == '+' or i == '-' or i == '*' or i =='/':
                b = s.pop()
                a = s.pop()

                if i == '+':
                    s.append(a+b)
                elif i == '-':
                    s.append(a-b)
                elif i == '*':
                    s.append(a*b)
                elif i == '/':
                    s.append(int(float(a)/b))
            else:
                s.append(int(i))

        return s[-1]
        