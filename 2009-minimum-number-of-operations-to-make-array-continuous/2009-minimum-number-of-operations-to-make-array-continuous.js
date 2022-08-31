/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    
  const set = [...new Set(nums)]

    set.sort((a, b) => a - b)
    let min = nums.length
    for(let i = 0; i < set.length; i++){
        let end  = bs(set, set[i] + nums.length-1) + 1
        let curr = nums.length  - (end - i ) 
        min = Math.min(curr, min) 
        
        
    }
    return min
    
};

function bs(arr, target){
    let l = 0
    let r = arr.length -1
    while(l < r){
    
     let m = Math.ceil((l+r) / 2)
     if(arr[m] <= target)
         l = m
      else r = m-1
        
    
    }
    
    return l 
}








