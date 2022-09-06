/**
 * @param {number[]} nums
 * @return {boolean}
 */

class UnionFind {
    constructor(arr){
        this.parent = arr.reduce((a, b) => {
          a[b] = b
          return a
    }, {})
    }
     find = (x) => {
        if(this.parent[x] !== x) 
         this.parent[x] = this.find(this.parent[x])
        return this.parent[x]
    }

   union = (a, b) =>{
        let pa = this.find(a)
        let pb = this.find(b)
        if(pa !== pb)
            this.parent[pb] = pa
   }
     

}

function seive(union, max, numsSet){
    let p = 2
    const primes = Array(max + 1).fill(true)
    while (p < max){
        let prev = 0
        if(primes[p] ) {
        for(let i = p ; i < max; i+= p){
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

}
var gcdSort = function(nums) {
    
    const  numsSet = new Set(nums)
    const  numsSorted = [...nums].sort((a, b) => a - b)
    let    max = numsSorted[numsSorted.length - 1] + 1
    const {union, find} = new UnionFind(numsSorted)
    seive(union, max, numsSet)
    for(let  i = 0; i< nums.length; i++)
        if(find(nums[i]) !== find(numsSorted[i]))
            return false
    
    return true
};