class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ''
        
        for i, c  in enumerate(s):
            if i == len(s)//2:
                break
            if c > "a":
                return s[:i] + "a" + s[i+1:]
        return s[:-1] + "b"