/**
 * @param {number[]} nums
 * @return {boolean}
 */

class UnionFind {
    constructor(arr, max){
        this.parent = arr.reduce((a, b) => {
          a[b] = b
          return a
    }, {})
        this.sizes = {}
        this.max = arr.length > 0 ? 1 : 0
    }
     find = (x) => {
        if(this.parent[x] !== x) 
         this.parent[x] = this.find(this.parent[x])
        return this.parent[x]
    }

   union = (a, b) =>{
        let pa = this.find(a)
        let pb = this.find(b)
        if(pa !== pb){
            this.parent[pb] = pa
            this.sizes[pa] = this.sizes[pa] || 1
            this.sizes[pa] += (this.sizes[pb] || 1)
            this.max = Math.max(this.max, this.sizes[pa])
        }
   }
     

}

function seive(union, max, numsSet){
    let p = 2
    const primes = Array(max + 1).fill(true)
    while (p < max){
        let prev = 0
        if(primes[p]) {
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
var largestComponentSize = function(nums) {
    
    const  numsSet = new Set(nums)
    let    max = Math.max(...nums) + 1
    const unionFind = new UnionFind(nums , max)
    const {union, find} = unionFind
    seive(union, max, numsSet)
    return unionFind.max
};