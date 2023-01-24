class Solution:
    def numberOfWays(self, corridor: str) -> int:
        count = Counter(corridor)
        if  count["S"] <= 2:
            return count['S'] // 2
        if count["S"] % 2:
            return 0
        s = 0
        f = 0
        res = 1
        
        for c in corridor:
            if c == "S":
                s += 1
            if s % 2 == 1 and s > 2 and c == "S":
                res *= ( f + 1)
            if c == "S":
                f = 0
            else :
                f += 1

        return res % (10 ** 9 + 7)
                
                