class Solution:
    def makeFancyString(self, s: str) -> str:
        
        
        p = pp = res = ''
        
        for c in s:
            if c != p or c != pp :
                res += c
            p , pp = c, p
        return res
                