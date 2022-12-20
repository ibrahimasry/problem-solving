class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def level(node):
            res = 0
            while node:
                node //= 2
                res += 1
            return res
        def low(a , b):
            level1 = level(a)
            level2 = level(b)
            if level2 > level1:
                a,b=b,a
                level1,level2=level2,level1
            while level1 > level2:
                level1 -= 1
                a //= 2
            while a != b:
                a //= 2
                b //= 2
            return a
        res = []
        for a, b in queries:
            lca = low(a,b)
            res.append((level(a) + level(b) - 2 * level(lca)) + 1)
        return res