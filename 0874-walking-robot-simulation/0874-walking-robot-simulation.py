class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        seen = set([(x,y) for x , y in obstacles])
        dir = 3
        dirs = [(1,0),(0,-1),(-1,0),(0,1)]
        x,y = 0,0
        res = 0
        for c in commands:
            if c < 0:
                if c == -2:
                    dir = ((dir-1) + 4) % 4
                else :
                    dir = (dir+1) % 4
            else :
                i, j = dirs[dir]
                nx , ny = x,y
                while c:
                    if (nx+i,ny+j) in seen:
                        break
                    nx,ny = nx+i,ny+j
                    c -= 1
                    
                x,y = nx,ny
                res = max(res, x**2 + y ** 2)
        return res