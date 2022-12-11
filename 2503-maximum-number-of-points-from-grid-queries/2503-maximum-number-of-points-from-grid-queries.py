class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        pq = [(grid[0][0], 0,0)]
        
        queries = sorted([(v, i) for i, v in enumerate(queries)])
        l = len(queries)
        ans = [0] * l
        level = 0
        seen = set()
        seen.add((0,0))
        for v, i in queries:
            
            while pq and pq[0][0] < v:
                _ , r, c = heapq.heappop(pq)
                level += 1
                for x, y in [[-1,0],[0,-1],[1,0],[0,1]]:
                    nx , ny = r+x  , c + y
                    if  0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                        heapq.heappush(pq, (grid[nx][ny], nx, ny))
                        seen.add((nx, ny))
            ans[i] = level
        return ans