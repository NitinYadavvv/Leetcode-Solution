# Last updated: 1/18/2026, 6:19:00 PM
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        h = {}
        for ch in s1:
            if ch in h:
                h[ch]+=1
            else:
                h[ch]=1
        i = 0
        j = len(s1)-1
        while j<len(s2):
            h1 = {}
            k = i
            while k<=j:
                if s2[k] not in h1:
                    h1[s2[k]] = 1
                else:
                    h1[s2[k]]+=1
                k+=1
            if h1 == h:
                return True
            i+=1
            j+=1
        return False
        





        