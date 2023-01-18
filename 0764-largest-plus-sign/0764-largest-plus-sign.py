class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        up = [[[0,0]] * (n+1) for _ in range(n+1)]
        seen = set((i,j) for i , j in mines)
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i-1,j-1) in seen:
                    continue
                else:
                    up[i][j] = [up[i-1][j][0] + 1 , up[i][j-1][1] + 1]
        down = [[[0,0]] * (n+1) for _ in range(n+1)]
        
        
        for i in range(n-1, -1,-1):
            for j in range(n-1,-1,-1):
                if (i,j) in seen:
                    down[i][j] = [0,0]
                else:
                    down[i][j] = [down[i+1][j][0] + 1, down[i][j+1][1] + 1]
        res = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
               res = max(res,min(min(down[i-1][j-1]), min(up[i][j])))
        return res