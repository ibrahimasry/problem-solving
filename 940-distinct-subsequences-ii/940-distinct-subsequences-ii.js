/**
 * @param {string} s
 * @return {number}
 */
var distinctSubseqII = function(s) {
    
    const last = {}
    const dp = Array(s.length + 1).fill(1)
    const mod =( 10 ** 9) + 7
    
    for(let i = 1; i<= s.length; i++){
        let j = last[s[i-1]] === undefined ? -1 : last[s[i-1]]
        let dup = 0            
         if(j > 0)
         dup = dp[j-1]
        
         last[s[i-1]] = i
         dp[i] = dp[i-1] * 2 - dup
         dp[i] %= mod
        
    }
    
    return (dp[dp.length -1] - 1 + mod ) % mod
    
};