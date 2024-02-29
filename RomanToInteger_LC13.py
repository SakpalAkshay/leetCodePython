class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,  'V':5, 'X':10, 'L':50,  'C':100,  'D':500, 'M':1000}
        op = 0
        for i in range(len(s)):
            #checking for Index error
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                op -= values[s[i]]
            else:
                op += values[s[i]]

        return op 


