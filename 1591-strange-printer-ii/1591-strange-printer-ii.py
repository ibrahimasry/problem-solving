class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        
        def dfs(c):
            if  c in printing:
                return False
            if c in printed:
                return True

            for i in range(border[c][0] , border[c][1] + 1):
                for j in range(border[c][2], border[c][3] + 1):
                    curr = targetGrid[i][j]
                    if curr == c : continue
                    printing.add(c)

                    if not dfs(curr):
                        return False
                    printing.remove(c)
            printed.add(c)
            return True
        border = {}
        
        n = len(targetGrid)
        m = len(targetGrid[0])
        
        for i in range(n):
            for j in range(m):
                c = targetGrid[i][j]
                if c not in border:
                   border[c] = (i, i, j, j)
                else:
                    i1, i2, j1, j2 = border[c]
                    border[c] = (min(i1, i) , max(i2, i) , min(j1, j), max(j2, j))
        printing = set()
        printed = set()
        for c in border.keys():

            if c not in printed:
                if not dfs(c):
                    return False
        return True
        