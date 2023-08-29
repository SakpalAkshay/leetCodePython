'''Given a string s consisting of words and spaces, return the length of the last word in the string.'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = s.strip()
        newStr = str.split(" ")
        return len(newStr[-1])
