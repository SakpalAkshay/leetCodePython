class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''.join(letter for letter in s if letter.isalnum()).lower()
        left, right = 0, len(newStr) - 1

        while left <= right:
            if newStr[left] != newStr[right]:
                return False
            left +=1
            right-=1
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
       
        def check(i,s):
            if i >= len(s) // 2:
                return True
            
            if s[i] != s[len(s) - i -1]:
                return False

            return check(i+1,s)
        
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        if len(s) < 1:
            return True
        return check(0, s)

        
