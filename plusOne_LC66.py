'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        summation = 0
        length = len(digits)
        for i in digits:
            summation += i * pow(10,length-1)
            length = length - 1
        summation +=1

        newStr = str(summation)
        l = []
        for i in newStr:
            l.append(int(i))
        return l

    def secondPlusOne(self, digits: List[int]) -> List[int]:
        strg = ''
        for i in digits:
            strg+= str(i)
        numStr = int(strg)
        numStr +=1
        l = []
        for i in str(numStr):
            l.append(int(i))
        return l
