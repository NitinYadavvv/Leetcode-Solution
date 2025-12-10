# Last updated: 12/10/2025, 8:24:50 AM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in pairs.values():  # opening brackets
                stack.append(ch)
            else:  # closing brackets
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        
        return not stack  # True if empty, False otherwise
