class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        
        def dfs(r, c):
            if r < len(land) and c < len(land[0]) and land[r][c]:
               land[r][c] = 0
               r1, c1 = dfs(r+1, c)
               r2, c2 = dfs(r, c+1)
               return [max(r2,r1,r), max(c2,c1,c)]
            return [-1,-1]
        r = len(land)
        c = len(land[0])
        
        ans = []
        
        
        for i in range(r):
            for j in range(c):
                
                if land[i][j] != 0 :
                    ans.append([i,j] + dfs(i , j))
        return ans