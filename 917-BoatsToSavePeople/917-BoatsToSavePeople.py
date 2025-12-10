# Last updated: 12/10/2025, 8:21:37 AM
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        res = 0
        i = 0
        j = len(people)-1
        people.sort()
        while j>=i:
            res+=1
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            elif people[i]>people[j] and people[i]<=limit:
                i+=1
            else:
                j-=1
        return res

        