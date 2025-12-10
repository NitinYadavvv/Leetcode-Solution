# Last updated: 12/10/2025, 8:21:35 AM
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        s = {}
        res= 0 
        j = 0
        for i in range(len(fruits)):

            if fruits[i] not in s: 

                while len(s)==2 and s[fruits[j]]>0:
                    s[fruits[j]]-=1
                    if s[fruits[j]] == 0:
                        del s[fruits[j]]
                    j+=1

                s[fruits[i]]=1
                res = max((i-j+1),res)

            else:
                res = max((i-j+1),res)
                s[fruits[i]]+=1
        res = max((i-j+1),res)
        return res
        