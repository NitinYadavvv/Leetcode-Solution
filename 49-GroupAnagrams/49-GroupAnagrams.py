# Last updated: 12/12/2025, 9:05:55 PM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h ={}
        res = []
        for i in strs:
            s = tuple(sorted(i))
            if s not in h:
                h[s] = [i]
            else:
                h[s].append(i)
        return list(h.values())




    



        