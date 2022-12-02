/**
 * @param {string} s
 * @return {number}
 */
var numberOfWays = function(s) {
    const p1 = "101"
    const p2 = "010"
    const dp1 = Array(4).fill(0)
    const dp2 = Array(4).fill(0)
    dp1[3] = dp2[3] = 1
    
    for (let c of s)
        for(let i = 0; i< 3; i++){
            if (p1[i] == c)
                dp1[i] += dp1[i+1]
            if (p2[i] == c)
                dp2[i] += dp2[i+1]
        }
    return dp1[0] + dp2[0]
    
};