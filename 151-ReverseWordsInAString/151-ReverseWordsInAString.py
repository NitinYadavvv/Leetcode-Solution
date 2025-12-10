# Last updated: 12/10/2025, 8:22:42 AM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        text = s.split()
        str = ""
        i = len(text)-1
        while i>=0:
            if i != 0:
                str += text.pop(i)+" "
            else:
                str += text.pop(i)
            i-=1  
                  
        return str
        

        