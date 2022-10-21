class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        def find(x) :
            if parents[x] != x :
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parents[px] = py
        
        n = len(matrix)
        m = len(matrix[0])
        
        rowMax = [0] * n
        colMax = [0] * m
        
        ans = [[0] * m for _ in range(n)]
        
        valToIdx = defaultdict(list)
        for i in range(n):
            for j in range(m):
                val = matrix[i][j]
                valToIdx[val].append((i, j))
        
        for val in sorted(valToIdx):
            parents = list(range(m+n))

            for i, j  in valToIdx[val] :
                union(i, j + n)
            rootToRank = defaultdict(int)
            for i, j  in valToIdx[val] :
                parent = find(i)
                rootToRank[parent] = max(rootToRank[parent], max(rowMax[i], colMax[j]) + 1)
            for i, j  in valToIdx[val] :
                parent = find(i)
                ans[i][j] = rootToRank[parent]
                rowMax[i] = max(rowMax[i], rootToRank[parent])
                colMax[j] = max(colMax[j] , rootToRank[parent])
        return ans