/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var closestPrimes = function(left, right) {
        const primes = Array(right + 1).fill(true)
        let n1 = 1
        let n2 = -1 , prev = -1
        
        for(let i = 2; i <= right; i++){
            if (primes[i]){
                if (i >= left){
                    if (prev != -1){
                        if (n2 - n1 > i - prev || (n2 * n1 < 0))
                            [n1 , n2] = [prev , i]
                    }
                    prev = i
                }
            }
                for(let j = i*i; j <= right; j += i)
                    primes[j] = false
        }
        if (n2 * n1 < 0)
            return [-1,-1]
        return [n1 , n2]
        
    
};