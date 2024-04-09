import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(6000)
        dicts = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        sums = 0
        c = len(num1)
        d = len(num2)
        for i in range(len(num1)):
            sums += dicts[num1[i]] * (10**(c-i-1))
            
        for j in range(len(num2)):
            sums += dicts[num2[j]] * (10**(d - j - 1))

        return str(sums)

    def addStrings2(self, num1: str, num2: str) -> str:
        res = []
      
        carry = 0
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        if len(num2) > len(num1):
            num1 = '0' * (len(num2) - len(num1)) + num1
        p1,p2 = len(num1)-1, len(num2)-1
        while p1 >= 0 and p2 >= 0:
            num = carry + int(num1[p1]) +int(num2[p2])
            if num < 10:
                carry = 0
                res.append(str(num))
            else:
                carry = 1
                res.append(str(num%10))
            p1 -= 1
            p2 -= 1
        if carry > 0:
            res.append(str(carry))
        return ''.join(reversed(res))

