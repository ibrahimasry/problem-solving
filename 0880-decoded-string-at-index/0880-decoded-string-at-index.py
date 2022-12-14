class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else :
                size += 1
        n = len(s)
        
        for c in s[::-1]:
            k %= size
            
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else :
                size -= 1
        