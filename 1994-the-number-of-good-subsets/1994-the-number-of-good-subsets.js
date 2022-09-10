/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubsets = function(nums) {
    
    const primes = []
    
    for(let i = 2; i < 31; i++)
 {

     let isPrimes = true
     for(let j = 2; j < i; j++){
            if(i % j == 0)
                {
                    isPrimes = false
                }
        }
     if(isPrimes)
         primes.push(i)
}
    const count = {}
    for(let c of nums){
        count[c] = count[c] || 0
        count[c]++
    }
    nums = Object.keys(count).map((a) => +a)
    const mod = 10 ** 9 + 7
    let ones = BigInt(1)
    for (let i = 0; i < count[1] || 0; i++) {
      ones *= 2n;
      ones %= BigInt(mod);
    }
    const ans = (BigInt((dfs(nums, primes, count ,  0 , 0 , {}) - 1))) * ones
    return ans % BigInt(mod)
      
};


function dfs(nums, primes, count, i, mask, cache){
    if(i == nums.length)
        return 1
    let ans = 0 
    let hash = mask + "-" + i
    if(cache[hash] !== undefined)
        return cache[hash]
    ans += dfs(nums, primes, count , i + 1,  mask , cache)
    let key = nums[i]
    if(key != 1){
        let curr = 0
        for(let j = 0; j < primes.length; j++){
            let p = primes[j]
            if(key % p === 0)
                {
                    curr |= (1 << j)
                }
        }
        if(key % 4 !== 0 && key % 9 !== 0 && key % 25 !== 0 && ((mask & curr) === 0)){
            ans += (dfs(nums, primes, count, i+1, mask | curr, cache)) * count[key] 

        } 
        
        
        
        
    }
            cache[hash]  = ans % 1000000007
           return cache[hash]
    
}