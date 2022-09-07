/**
 * @param {number} n
 * @param {number} threshold
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var areConnected = function(n, threshold, queries) {
    const parent = Array(n + 1).fill(-1).map((_, i)=> i)
    const find = (x)=> {
        if(parent[x] !== x)
            parent[x] = find(parent[x])
        return parent[x]
    }
    const union = (a, b) => {
        const pa = find(a)
        const pb = find(b)
        if(pa !== pb)
            parent[pa] = pb
    }
    for(let i = threshold + 1; i <= n; i++){
        for(let j = i * 2; j <= n; j+=i)
            union(i, j)
    }
    
    return queries.map(([x, y]) => find(x) === find(y))
};