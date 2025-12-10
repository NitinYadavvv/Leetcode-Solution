# Last updated: 12/10/2025, 8:24:55 AM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        first = strs[0]

        for i in range(len(first)):
            char = first[i]
            for s in strs[1:]:
                # if mismatch or index out of range
                if i >= len(s) or s[i] != char:
                    return prefix
            prefix += char   # all strings matched at this index

        return prefix
        