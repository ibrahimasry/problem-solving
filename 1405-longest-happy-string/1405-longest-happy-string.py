class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def dfs(a,b,c,aa,bb,cc):
            if b > a:
                return dfs(b,a,c,bb,aa,cc)
            if c > b:
                return dfs(a,c,b,aa,cc,bb)
            if b == 0:
                
                return  min(2, a) * aa
            usedA = min(a, 2)
            usedB = 1 if a-usedA >= b else 0
            return usedA * aa + usedB * bb + dfs(a-usedA, b-usedB,c,aa,bb,cc)
        return dfs(a,b,c,'a','b','c')