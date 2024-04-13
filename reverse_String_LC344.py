class Solution:
    def reverseString(self, s: List[str]) -> None: 
        start= 0 
        end = len(s) - 1
        temp = 0
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start = start + 1
            end = end - 1
        return s
