class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        j = 0
        i = 0

        if s == "":
            return True

        while i < len(t):
            if s[j] == t[i]:
                j+=1
                if j > len(s) -1:
                    return True
            i+=1
        
        return False
