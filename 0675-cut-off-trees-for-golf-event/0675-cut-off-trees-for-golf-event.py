class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        noOfRows = len(forest)
        noOfColumns = len(forest[0])
		
		#step 1 
		
        trees = [ (forest[i][j], i, j) for i in range(noOfRows) for j in range(noOfColumns) if forest[i][j] > 1 ]
        trees = sorted(trees)
		
		#Implementation of step 3 BFS
		
        def bfs(row,col,treeX,treeY) :
            visited = [ [False for j in range(noOfColumns)] for i in range(noOfRows)]
            queue = deque([])
            queue.append( (row,col,0) )
            while queue :
                currX,currY,currSteps = queue.popleft()
                if (currX == treeX) and (currY == treeY) :
                    return currSteps 
                for r,c in [ (currX + 1,currY), (currX - 1,currY), (currX,currY + 1), (currX,currY - 1) ] :  
                    if (r >= 0) and (r < noOfRows) and (c >= 0) and (c < noOfColumns) and (not visited[r][c]) and (forest[r][c] > 0) :
                        visited[r][c] = True 
                        queue.append( ( r, c, currSteps + 1)  )
            return -1 
        
        x = 0
        y = 0 
        totalSteps = 0 
		
		#step 2 
		
        for tree in trees :
            steps = bfs(x,y,tree[1],tree[2]) #step 3 
            if steps < 0 :
                return -1 
            totalSteps += steps 
            x = tree[1]
            y = tree[2]
            
        return totalSteps 
