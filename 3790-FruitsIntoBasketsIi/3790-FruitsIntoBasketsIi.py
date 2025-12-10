# Last updated: 12/10/2025, 8:20:55 AM
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        cnt = 0
        for i in range(len(fruits)):
            boo = False
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    boo = True
                    baskets.remove(baskets[j])
                    break
            if(boo == False):
                cnt+=1    
        return cnt

