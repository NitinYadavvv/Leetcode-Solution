# Last updated: 2/26/2026, 7:47:21 AM
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        h = {}
        for i in bulbs:
            if i not in h:
                h[i] = 1
            else:
                if h[i] == 1:
                    h[i] = 0
                else:
                    h[i] = 1

        ans = []
        for i in h:
            if h[i] == 1:
                ans.append(i)
        ans.sort()
        return ans