class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(start, target):
            q = deque([start])
            dist = [[sys.maxsize] * n for _ in range(m)]
            dist[start[0]][start[1]] = 0
            while q:
                i,j = q.popleft()
                if forest[i][j] == target:
                    return dist[i][j]
                for x,y in [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]:
                    if 0 <= x < len(forest) and 0 <= y < len(forest[0]) and dist[x][y] == sys.maxsize and forest[x][y] != 0:
                        q.append([x,y])
                        dist[x][y] = dist[i][j] + 1
            return -1
        ans = 0
        
        n = len(forest[0])
        m = len(forest)
        tree = sorted((val,i,j) for i,row in enumerate(forest) for j, val in enumerate(row) if val > 1)[::-1]
        ans = 0
        start = [0,0]
        
        while tree:
            target , i , j = tree.pop()
            dist = bfs(start,target)
            if dist == -1:
                return -1
            start = [i,j]
            ans += dist
            
        return ans
            