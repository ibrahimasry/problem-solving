class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        
        n = len(grid)
        m = len(grid[0])
        dirs = {1:[0, 1], 2:[0, -1], 3:[1, 0], 4:[-1,0]}
        
        for i in range(n):
            for j in range(m):
                for d in dirs:
                    w = (0 if grid[i][j] == d else 1 )

                    ni = i + dirs[d][0]
                    nj = j + dirs[d][1]
                    if 0 <= ni < n and 0 <= nj < m :
                        graph[(i, j)].append((ni, nj, w))
        cost = {(i, j) : sys.maxsize for i in range(n)  for j in range(m)}
        
        cost[(0,0)] = 0
        pq = [(0, 0, 0)]
        seen = set()
        while len(pq) > 0:
            w, i, j = heapq.heappop(pq)
            if (i, j) in seen :
                continue
            if (i, j) == (n-1, m-1):
                return w
            seen.add((i,j))
            for x, y, w2 in graph[(i, j)]:
                total = w + w2
                if (x, y) not in seen and total < cost[(x, y)]:
                    heapq.heappush(pq, (total, x, y))
                    cost[(x, y)] = total
        return cost[(n-1, m-1)]