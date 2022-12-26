class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def dfs(a,b,aa,bb):
            if bb > aa:
                return dfs(b,a,bb,aa)
            if bb == 0:
                return a * aa
            usedA = min(2,aa)
            usedB = 1 if aa - usedA >= bb else 0
            return usedA * a + usedB * b + dfs(a,b,aa-usedA,bb-usedB)
        return dfs('a','b' , a,b)
                