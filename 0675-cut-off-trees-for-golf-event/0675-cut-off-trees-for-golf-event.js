/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
        let n = forest[0].length
        let m = forest.length
        const dirs = (i,j) => [[i,j-1],[i,j+1],[i-1,j],[i+1,j]]
        const mat = (m,n) => Array(m).fill(0).map(row => Array(n).fill(Infinity))
        const tree = []
        forest.forEach((row,i) => row.forEach((e,j) => e > 1 && tree.push([e,i,j])))
        tree.sort((a,b)=> b[0] - a[0])

        
        let ans = 0
        let start = [0,0]
        while (tree.length){
            const [target , i , j] = tree.pop()
            if (start[0] == i && start[1] == j)
                continue
            
            const dist = bfs(start,target)
            if (dist == -1)
                return -1
            start = [i,j]
            ans += dist
        }
        return ans
    
    
          function bfs(start, target){
            const q = new Queue();
            q.push(start)
            const dist = mat(m,n)
            dist[start[0]][start[1]] = 0
            const neis = (i,j) => dirs(i,j).filter(([x,y])=> 0 <= x && x < m && 0 <= y  && y < n && dist[x][y] == Infinity && forest[x][y] != 0)

            while (!q.isEmpty()){
               let [i,j] = q.dequeue()
                for (const [x,y] of neis(i,j)){
                    q.push([x,y])
                    dist[x][y] = dist[i][j] + 1
                    if (target == forest[x][y])
                        return dist[x][y]
            }
        }
            return -1
     }

            
    
};