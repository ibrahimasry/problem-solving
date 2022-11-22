/**
 * @param {string} s
 * @param {number} k
 * @param {number} minLength
 * @return {number}
 */
var beautifulPartitions = function(s, k, minLength) {
    
        const primes =  new Set([2, 3, 5, 7])
        const n = s.length
        const parts = [0]
        if (!primes.has(+s[0]) || primes.has(+s[n-1]))
            return 0
        for (let i = 1; i < n; i++)
            if (!primes.has(+s[i-1]) && primes.has(+s[i]))
                parts.push(i)
        parts.push(n)
        let dp = Array(parts.length).fill(0)
        dp[0] = 1
        for (let i = 1; i <= k ; i++){
           const curr = Array(parts.length).fill(0)
             for (let j = 1; j < parts.length; j++)
                for (let m = 0; m < j; m++){
                    if (parts[j] - parts[m] >= minLength)
                        curr[j] = (curr[j] + dp[m])  % (10 ** 9 + 7)
                }
            dp = curr
        }
        return dp[parts.length-1] % (10 ** 9 + 7)
            
    
};