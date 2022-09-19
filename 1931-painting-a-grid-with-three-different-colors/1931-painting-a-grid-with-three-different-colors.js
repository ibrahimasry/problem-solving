/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var colorTheGrid = function(m, n) {
    
    const  getColor = (col , mask) => ((mask >> (col * 2)) & 3)
    const  setColor = (color, col, mask) => {
        const oldColor = getColor(col , mask)
        return   ((mask ^ ( oldColor << (col* 2))) | (color << (col * 2)))
    }
    const mod = BigInt(10 ** 9 + 7)

    const  dfs = (i, lastRow, cache) => { 
        if( i == m * n) return 1n
        const key = lastRow + "$" + i
        if(cache[key] !== undefined) return cache[key]
        let row = Math.floor(i / m)
        let col = i % m
        const  neighbours = new Set()
        if (row > 0)
            neighbours.add(getColor(col , lastRow))
        if (col > 0)
            neighbours.add(getColor(col-1 , lastRow))
        let  res = 0n
        for (let color of [0, 1, 2])
            if (!neighbours.has(color)){
                res +=  (dfs(i+1, setColor(color, col, lastRow) , cache))
            }
        cache[key] = res 
        return res
    }

    return dfs(0, 0 , {})  % mod
    
};