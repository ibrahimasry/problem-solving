/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    
    const dp = grid[0].slice(0).fill(0)
    for(let i =0; i <  grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
            if(i === 0 && j === 0) {
                            dp[j] += grid[i][j]

                continue
            }
            const up = i === 0 ? Infinity : dp[j]
            const left = j === 0? Infinity : dp[j-1]
            dp[j] = Math.min(up, left) + grid[i][j]
        }
    }
    
    return dp[grid[0].length -1]
};