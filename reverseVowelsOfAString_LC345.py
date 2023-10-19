class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        left = 0 
        right = len(s) - 1
        listStr = list(s)

        while left <right:
            if listStr[left] in vowels and listStr[right] in vowels:
                listStr[left], listStr[right] = listStr[right], listStr[left]
            
                left+=1
                right-=1
            elif listStr[left] in vowels and listStr[right] not in vowels:
                right -=1
            else:
                left+=1
        
        return ''.join(listStr)
        
