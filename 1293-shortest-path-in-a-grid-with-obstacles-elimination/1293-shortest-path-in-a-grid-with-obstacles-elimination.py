class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        seen =  set()
        
        queue = deque()
        queue.append((0,0,k))
        seen.add((0,0,k))
        ans = 0
        while queue:
            currLevel = deque()
            for i, j , currK in queue:
                if (i,j) == (m-1, n-1):
                    return ans
                for x, y in [[i-1, j], [i+1,j], [i,j+1], [i, j-1]]:
                    if 0 <= x < m and 0 <= y < n :
                        if currK > 0 and grid[x][y] == 1:
                            if (x, y , currK-1) not in seen:
                                currLevel.append((x,y,currK-1))
                                seen.add((x, y, currK-1))
                        elif grid[x][y] == 0:
                            if (x, y , currK) not in seen:

                                currLevel.append((x, y, currK))
                                seen.add((x, y, currK))
            ans += 1
            queue = currLevel
        return -1