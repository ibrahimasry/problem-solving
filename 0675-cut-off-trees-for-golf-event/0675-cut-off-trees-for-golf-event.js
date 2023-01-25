/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
        let n = forest[0].length
        let m = forest.length

        function bfs(start, target){
            const q = new Queue();
            q.push(start)
            const dist = Array(m).fill(0).map(row=> Array(n).fill(Infinity))
             dist[start[0]][start[1]] = 0
            while (q.size() > 0){
               let [i,j] = q.dequeue()
                if (forest[i][j] == target)
                    return dist[i][j]
                for (const [x,y] of [[i,j-1],[i,j+1],[i-1,j],[i+1,j]])
                    if (0 <= x && x < m && 0 <= y  && y < n && dist[x][y] == Infinity && forest[x][y] != 0){
                        q.push([x,y])
                        dist[x][y] = dist[i][j] + 1
                        if (target == forest[x][y])
                            return dist[x][y]
                    }
            }
            return -1
        }
        
        const tree = []
        for(let i = 0; i  < m; i++){
            for (let j = 0; j < n; j++){
                if (forest[i][j] > 1)
                    tree.push([forest[i][j], i, j])
            }
        }
        tree.sort((a,b)=> b[0] - a[0])
        let ans = 0
        let start = [0,0]
        
        while (tree.length){
            const [target , i , j] = tree.pop()
            const dist = bfs(start,target)
            if (dist == -1)
                return -1
            start = [i,j]
            ans += dist
        }
        return ans
            
    
};