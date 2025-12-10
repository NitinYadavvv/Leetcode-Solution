# Last updated: 12/10/2025, 8:21:54 AM
class Solution(object):
    def topKFrequent(self, nums, k):
        """ 
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i]+=1
        l = sorted(h.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in l[:k]:
            res.append(i[0])

        return res
        