class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def inside(x,y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                return True
            return False
        n = len(grid[0])
        m = len(grid)
        pq = []
        box = person = target = (-1,-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "S":
                    person = (i,j)
                if grid[i][j] == "T":
                    target = (i,j)
                if grid[i][j] == "B":
                    box = (i,j)
        heappush(pq,(0, person[0],person[1] , box[0],box[1]))
        dist = defaultdict(lambda: inf)
        while pq:
            moves , i,j,x,y = heappop(pq)
            if (x,y) == target:
                return moves
            if dist[(i,j,x,y)] < moves :
                continue
            for (dirx , diry) in [[-1,0],[1,0],[0,-1],[0,1]]:
                r, c = i+dirx , j+diry
                if inside(r,c) :
                    nx , ny = x,y
                    if (r,c) == (x,y):
                        nx,ny = x + dirx  , y + diry
                        if inside(nx,ny) and dist[(r,c,nx,ny)] > moves + 1:
                            dist[(r,c,nx,ny)] = moves + 1
                            heappush(pq,(moves+1,r,c,nx,ny))
                    else:
                        if dist[(r,c,nx,ny)] > moves :
                            dist[(r,c,nx,ny)] = moves 
                            heappush(pq,(moves,r,c,nx,ny))
                    
        return -1