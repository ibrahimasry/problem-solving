/**
 * @param {number[]} nums
 * @return {boolean}
 */
var gcdSort = function(nums) {
    
    const numsSet = new Set(nums)
    const  numsSorted = [...nums].sort((a, b) => a - b)
    let max = numsSorted[numsSorted.length - 1] + 1
    let p = 2
    const parent = nums.reduce((a, b) => {
          a[b] = b
          return a
    }, {})
    const primes = Array(max + 1).fill(true)
    while (p < max){
        let prev = 0
        if(primes[p] ) {
        for(let i = p ; i < max; i+=p){
            if(numsSet.has(i)){
               if(prev > 0)
                    union(i, prev)
                prev = i
            }
            primes[i] = false
        }
        }
        p++
    }
    for(let  i = 0; i< nums.length; i++)
        if(nums[i] != numsSorted[i] && find(nums[i]) !== find(numsSorted[i]))
            return false
    
    function union(a, b){
        let pa = find(a)
        let pb = find(b)
        if(pa !== pb)
            parent[pb] = pa
    }
    function find(x){
        if(parent[x] !== x) 
         parent[x] = find(parent[x])
        return parent[x]
    }
    return true
};