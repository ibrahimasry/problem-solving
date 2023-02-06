class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q = deque([[0,0,0]])
        seen = set()
        while q :
            x,y,steps = q.popleft()
            
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return steps
            for i,j in pairwise([-1,0,1,0,-1]):
                nx,ny = x+i, y + j
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx,ny) not in seen:
                    if grid[nx][ny]:
                        q.append((nx,ny,steps+1))
                    else:
                        q.appendleft((nx,ny,steps))
                    seen.add((nx,ny))
        return -1