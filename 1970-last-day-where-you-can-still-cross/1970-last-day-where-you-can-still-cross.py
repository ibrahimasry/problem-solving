class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def good(days):
            mat = [[0] * col for _ in range(row)]
            for i in range(days):
                mat[cells[i][0]-1][cells[i][1]-1] = 1
            q = deque()
            for j in range(col):
                if mat[0][j] == 0:
                    q.append((0,j))
                    mat[0][j] = 1
            while q:
                i,j = q.popleft()
                if i == row-1:
                    return True
                dirs = [1,0,-1,0]
                for d in range(4):
                    x = dirs[d]
                    y = dirs[(d+1)%4]
                    r = i + x
                    c = j + y
                    if 0 <= r < row and 0 <= c < col and mat[r][c] == 0:
                        q.append((r,c))
                        mat[r][c] = 1
            return False
        
        
        l = 1
        r = len(cells)
        while l < r:
            m = (l+r+1)>>1
            if good(m):
                l = m
            else:
                r = m - 1
        return l