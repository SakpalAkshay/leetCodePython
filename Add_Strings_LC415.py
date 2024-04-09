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

