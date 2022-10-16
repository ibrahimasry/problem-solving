/**
 * @param {number[]} houses
 * @param {number} k
 * @return {number}
 */
var minDistance = function(houses, k) {
        const dist = Array(houses.length).fill(0).map(house => Array(houses.length).fill(0))
        
        
        const n = houses.length
        houses.sort((a, b) => a -b)
        for(let i = 0; i< n; i++){
            for(let j = i; j < n; j++)
            {
                let mid = houses[Math.floor((i + j) / 2)]
                for(let h = i; h <= j; h++)
                    dist[i][j] += Math.abs(mid - houses[h])
        }
        }
    const dp = (k, i , cache) => {
            if (k == 0 && i == n) 
                return 0
            if (k == 0 || i == n) 
                return Infinity
           const key = `${k}-${i}`
           if (key in cache) return cache[key]
           let ans = Infinity
            for(let j = i; j < n; j++)
                ans = Math.min(ans, dist[i][j] + dp(k-1, j+1, cache))
            cache[key] = ans
            return ans
    }
    
    return dp(k, 0, {})
};