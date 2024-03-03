class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenfirst = len(word1)
        lenSec = len(word2)
        newStr = ""
        i =0
        j=0
        while i < lenfirst and j < lenSec:
            newStr+= word1[i]
            newStr+= word2[j]
            i +=1
            j +=1
        
        while i < lenfirst:
            newStr+=word1[i]
            i+=1

        while j< lenSec:
            newStr+=word2[j]
            j+=1
        
        return newStr
