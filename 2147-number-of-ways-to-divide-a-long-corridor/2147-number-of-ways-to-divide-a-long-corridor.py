class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s = 0
        f = 0
        res = 1
        mod = (10 ** 9 + 7)
        
        for c in corridor:
            if c == "S":
                s += 1
                if s % 2 == 1 and s > 2:
                    res *= (f + 1) 
                    res %= mod
                f = 0
            else :
                f += 1

        return res if s >= 2 and s % 2 == 0 else 0
                
                