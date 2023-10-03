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


        
