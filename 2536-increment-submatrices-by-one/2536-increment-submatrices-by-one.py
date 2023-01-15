class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        
        for x1,y1,x2,y2 in queries:
            for i in range(x1,x2+1):
                mat[i][y1] += 1
            if y2 + 1 < n:
                for i in range(x1,x2+1):
                    mat[i][y2+1] -=1
                
        ans = [[0] * n for _ in range(n)]
        
        cnt  = 0
        
        for i in range(n):
            for j in range(n):
                cnt += mat[i][j]
                ans[i][j] = cnt
            cnt = 0
        return ans