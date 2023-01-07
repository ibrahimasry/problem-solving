class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        
        count = 0
        
        for c in s:
            if c == "|":
                count += 1
            elif c == "*":
                res += count % 2 == 0
        return res