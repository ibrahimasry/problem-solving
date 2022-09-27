/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */

let factorial = function(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    return n * factorial(n - 1);
};

var getPermutation = function(n, k) {
    
    let res = []
    let arr = []
    for(let i = 0; i < n; i++)
        arr[i] = i+1
      helper( k, arr, res)
    
    return res.join('')
    
};


function helper(k, arr, res){
    
    while(arr.length){
    let block = factorial(arr.length-1)
    let index = Math.ceil((k)/  block) -1
     res.push(arr[index])
      arr.splice(index, 1)
     k = k -  (block * index)
   }
    
}
