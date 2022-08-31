/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length
    const set = [...new Set(nums)].sort((a, b) => a - b)
    let min = n
    for(let i = 0; i < set.length; i++){
        let end  = bs(set, i , set[i] + n -1) 
        let curr = n  - (end - i  + 1)
        min = Math.min(curr, min) 
        
        
    }
    return min
    
};

function bs(arr,start ,  target){
    let l = start
    let r = arr.length -1
    while(l < r){
     let m = Math.ceil((l+r) / 2)
     if(arr[m] <= target)
         l = m
      else r = m-1
        
    
    }
    
    return l 
}








