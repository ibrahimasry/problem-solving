/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(s1, s2) {
        return helper(s1, s2, s1.length-1, s2.length-1, [])
    
};


function helper(s1, s2, m, n, cache){
    if(m < 0 && n < 0) return 0
    if(m < 0) return n +1
    if(n < 0) return m +1
        cache[m] = cache[m] || []

    if(cache[m][n]) return cache[m][n]
     cache[m][n] = Infinity
    let sum1 = Infinity
    let sum2 = Infinity
    let sum3 = Infinity
    if(s1[m] === s2[n])
        cache[m][n] = helper(s1, s2, m-1, n-1, cache)
  else {
     sum1 = 1 + helper(s1, s2, m-1, n,cache)
     sum2 = 1 + helper(s1, s2, m, n-1, cache)
     sum3 = 1 + helper(s1, s2, m-1, n-1, cache)

  }

    cache[m][n] = Math.min(sum1 ,sum2, sum3, cache[m][n] )
    return cache[m][n]
}


    
