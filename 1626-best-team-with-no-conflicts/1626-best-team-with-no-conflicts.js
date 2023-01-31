/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    const n = scores.length
    const dp = Array(n).fill(-1)
    let pairs = scores.map((v,i) => [ages[i],v]).sort((a,b)=> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0] )
    pairs = pairs.map(a=>a[1])
    for(let i = 0; i < n; i++){
        dp[i] = pairs[i]
        for(let j=0; j<i; j++){
            if(pairs[i] >= pairs[j])
                dp[i] = Math.max(dp[i], dp[j] + pairs[i])
        }
    }
    return Math.max(...dp)
    
};