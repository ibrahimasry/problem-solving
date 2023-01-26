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
            moves , personX ,personY, boxX,boxY = heappop(pq)
            if (boxX,boxY) == target:
                return moves
            if dist[(personX , personY, boxX, boxY)] < moves :
                continue
            for (dirx , diry) in [[-1,0],[1,0],[0,-1],[0,1]]:
                nextPersonX, nextPersonY = personX + dirx , personY + diry
                if inside(nextPersonX,nextPersonY) :
                    cost = (nextPersonX, nextPersonY) == (boxX,boxY)
                    nextBoxX , nextBoxY = boxX + dirx * cost  , boxY + diry * cost
                    key = (nextPersonX,nextPersonY, nextBoxX, nextBoxY)
                    if inside(nextBoxX , nextBoxY) and dist[key] > moves + 1:
                        dist[key] = moves + cost
                        heappush(pq,(moves+cost,*key))
                    
        return -1