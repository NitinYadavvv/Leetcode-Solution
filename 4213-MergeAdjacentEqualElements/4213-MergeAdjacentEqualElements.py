# Last updated: 2/12/2026, 10:51:00 PM
class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        

        stack = []
        for i in nums:
            stack.append(i)
            while len(stack)>1 and stack[-2] == stack[-1]:
                v = stack.pop()
                stack.pop()
                stack.append(v*2)
        return stack