class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        m = len(heights)
        n = len(heights[0])
        
        costs = [[inf] * n for _ in range(m)]
        costs[0][0] = 0
        dirs = [0,1,0,-1,0]
        
        pq = [[0,0,0]]
        
        while pq:
            prev , x, y = heapq.heappop(pq)
            if costs[x][y] > prev: 
                continue
            if x == m - 1 and y == n-1:
                return prev
            for i in range(4):
                nx, ny = x + dirs[i] , y + dirs[i+1]
                if 0 <= nx < m and 0 <= ny < n :
                    curr = max(prev, abs(heights[x][y] - heights[nx][ny]))
                    if costs[nx][ny]  > curr:
                        costs[nx][ny] = curr
                        heapq.heappush(pq, [curr , nx,ny])