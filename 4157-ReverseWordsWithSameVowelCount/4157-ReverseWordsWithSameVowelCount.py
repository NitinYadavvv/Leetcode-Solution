# Last updated: 12/16/2025, 10:35:50 AM
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = ['a','e','i','o','u']
        c = 0
        s = list(s)
        index = 0
        for i in range(len(s)):
            if s[i] == ' ':
                index = i
                break
            if s[i] in vow:
                c+=1

        if index == 0:
            return "".join(s)
        i = index+1
        
        
        while i<len(s):
            j = i
            count = 0
            while i<len(s) and s[i] != ' ':
                if s[i] in vow:
                    count+=1
                i+=1
            e = i-1 
            if count == c:
                while j<e:
                    s[e] , s[j] = s[j] , s[e]
                    j+=1
                    e-=1
            i+=1
        return "".join(s)                    
        