/**
 * @param {string} binary
 * @return {number}
 */
var numberOfUniqueGoodSubsequences = function(binary) {
    
    
    let i = 0
    const mod = 10 ** 9 +7
    while(i < binary.length && binary[i] != 1)
        i++
    if(i == binary.length)
        return 1
    
    let dp = Array(binary.length  ).fill(0)
    dp[i++] = 1
    const last = {}
    for(; i < binary.length; i++){
       const j = last[binary[i ]] === undefined ? -1 : last[binary[i]]
       
       let dup = 0
       if(j > 0)
           dup = dp[j -1]
        if(i > 0){
        dp[i] = dp[i-1] * 2 - dup
        dp[i] %= mod
    }
        last[binary[i]] = i
    }
    let hasZero = 0
    if(binary.split("").some((a) => a === "0"))
        hasZero += 1
    return( dp[dp.length - 1] + hasZero + mod) % mod
    
};