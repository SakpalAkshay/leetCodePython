'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

class Solution:
    def isPalindrome(self, x: int) -> bool:

        return str(x)==str(x)[::-1]



    def anotherSolution(self,x: int) -> bool:
        if x<0:
            return False

        n = x
        rev = 0
        while n != 0:
            left = n % 10
            n = n // 10
            rev = rev * 10 + left

        return rev == x
