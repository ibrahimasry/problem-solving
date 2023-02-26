class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        pq = [(0,0,0)]
        n,m = len(grid[0]), len(grid)

        dist = [[inf] * n for _ in range(m)]
        while pq:
            t , i , j = heappop(pq)
            if i == m-1 and j == n-1:
                return t

            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = i + x, j + y
                if 0 <= nx < m and 0 <= ny < n:
                    if dist[nx][ny] == inf :
                        if grid[nx][ny] > (t+1):
                            if i == 0 and j == 0:
                                continue
                            dist[nx][ny] = (grid[nx][ny]-(t)) + (t) + ((grid[nx][ny]-(t)) % 2 == 0)
                        else:
                            dist[nx][ny] = (t+1)
                        heappush(pq,(dist[nx][ny],nx, y +j))
        return -1