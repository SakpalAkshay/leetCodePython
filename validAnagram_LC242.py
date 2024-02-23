class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        if len(s) == 0 and len(t)==0:
            return True

        if len(s) != len(t):
            return False

        for i in s:
            if i not in sdict:
                sdict[i] = 1
            else:
                sdict[i] += 1
        for i in t:
            if i not in tdict:
                tdict[i] = 1
            else:
                tdict[i] += 1
        
        for i in t:
            if sdict.get(i) != tdict.get(i):
                return False
        
        return True
