# Last updated: 12/10/2025, 8:21:08 AM
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in nums:
            stack.append(num)
            # keep merging while last two are non-coprime
            while len(stack) > 1 and self.gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.lcm(a, b))
        return stack

    def gcd(self, x, y):
        # Euclidean algorithm (efficient)
        while y:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return (x * y) // self.gcd(x, y)
