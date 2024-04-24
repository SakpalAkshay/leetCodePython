
class Solution:
    def addDigits(self, num: int) -> int:
        if num ==0:
            return 0

        while num >=10:
            n = num%10
            num = num//10
            num = num + n 
        return num
        
