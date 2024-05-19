class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 !=0:
            return False
        elif n <=0:
            return False
        else:
            num = n

            count = 0
            while n!=1:
                n = n//2
                count+=1
            if num == pow(2,count):
                return True

