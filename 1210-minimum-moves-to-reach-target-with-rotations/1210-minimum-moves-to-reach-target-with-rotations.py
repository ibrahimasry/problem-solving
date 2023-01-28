class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        q = deque([(0,0 , 0 , 1)])
        seen = set()
        seen.add(q[0])
        steps = 0
        n = len(grid)
        while q:
            for _ in range(len(q)):
                r,c,r1,c1 = q.popleft()
                if (r,c,r1,c1) == (n-1,n-2,n-1,n-1):
                    return steps 
                hor = r == r1
                ver = c == c1
                if ver:
                    if c1 + 1 < n and grid[r1][c1+1] == 0 and grid[r][c+1] == 0:
                        q.append((r,c+1,r1,c1+1))
                        if q[-1] in seen:
                            q.pop()
                        seen.add(q[-1])
                    if  r1 + 1 < n and grid[r1+1][c] == 0 and grid[r+1][c] == 0:
                        q.append((r+1,c,r1+1,c))
                        if q[-1] in seen:
                            q.pop()
                        seen.add(q[-1])

                    if  c1 + 1 < n  and  grid[r1][c1+1] == 0 and grid[r][c1+1] == 0 :
                        q.append((r,c,r,c1 + 1))
                        if q[-1] in seen:
                            q.pop()
                        seen.add(q[-1])


                elif hor:
                    if c1 + 1 < n and grid[r1][c1+1] == 0 :
                        q.append((r,c+1,r1,c1+1))
                        if q[-1] in seen:
                            q.pop()
                        seen.add(q[-1])
                    if r+1 < n and grid[r1+1][c1] == 0 and grid[r+1][c] == 0:
                        q.append((r+1,c,r1+1,c1))
                        if q[-1] in seen:
                            q.pop()
                        seen.add(q[-1])

                    #clockwise
                    if r1 + 1 < n  and grid[r+1][c] == 0 and grid[r+1][c1] == 0:
                        q.append((r,c,r1+1,c1-1))
                        if q[-1] in seen:
                            q.pop()
                        seen.add(q[-1])


            steps += 1
        return -1