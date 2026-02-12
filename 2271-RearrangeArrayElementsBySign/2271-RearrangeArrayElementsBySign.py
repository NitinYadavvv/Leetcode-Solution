# Last updated: 2/12/2026, 10:51:38 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res