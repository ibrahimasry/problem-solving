/**
 * @param {string} s
 * @return {number}
 */
var distinctSubseqII = function(s) {
    
    const dp = {}
    const mod =( 10 ** 9) + 7
    
    for(let i = 0; i < s.length; i++){
        dp[s[i]]  = Object.values(dp).reduce((a, b)=> a  + b, 0) % mod + 1
        
    }
    
    return (Object.values(dp).reduce((a, b) => a  + b , 0) ) % mod
    
};