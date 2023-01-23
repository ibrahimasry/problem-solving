class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        q = deque(sorted([[v,i] for i,v in enumerate(queries)]))
        
        pq = [[grid[0][0],0,0]]
        ans = [0] * len(q)
        seen = set()
        seen.add((0,0))
        count = 0
        while q:
            while pq and pq[0][0] < q[0][0]:
                val,i,j = heapq.heappop(pq)
                count += 1
                for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x,y) not in seen:
                        heapq.heappush(pq, [grid[x][y], x, y])
                        seen.add((x,y))

            ans[q.popleft()[1]] =  count
        return ans