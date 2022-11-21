class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        costs = [[sys.maxsize] * n for _ in range(n)]
        
        seen = set()
        hq = [(grid[0][0], 0, 0)]
        seen.add((grid[0][0], 0,0))
        costs[0][0] = grid[0][0]
        while hq:
            cost, x, y = heapq.heappop(hq)
            if (x, y) == (n-1, n-1):
                return cost
            for i, j in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx = x + i
                ny = y + j
                if n > nx >= 0 and n > ny >= 0 :
                    currCost = cost + max(0, grid[nx][ny] - max(grid[x][y], cost)) 
                    if (currCost, nx, ny) not in seen and costs[nx][ny] > currCost :
                        costs[nx][ny] = currCost 
                        seen.add((currCost, nx, ny))

                        heapq.heappush(hq, (currCost, nx, ny))
        return costs[-1][-1]
                