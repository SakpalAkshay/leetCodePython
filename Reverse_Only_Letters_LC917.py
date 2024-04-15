class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst = list(s)
        i = 0
        j = len(lst) - 1
        while i < j:
            if lst[i].isalpha() and lst[j].isalpha():
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            else:
                if lst[i].isalpha()==False:
                    i +=1
                if lst[j].isalpha()==False:
                    j-=1
        
        return "".join(lst)
