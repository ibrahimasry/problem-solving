/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    let aux = nums.slice(0)
    merge(nums, aux, 0, nums.length -1)
    return nums
};

function merge(nums, aux, i, j){
    if( i >= j) return
    
    let m = Math.floor((i + j)/2)
    merge(aux, nums, i, m)
    merge(aux, nums, m + 1, j )
    let endLeft = m
    let endRight = j
    let startRight = m+1
    let startLeft = i
    let curr = startLeft
    while(startLeft <= endLeft && startRight <= endRight){
        if(aux[startLeft] < aux[startRight])
            nums[curr++] = aux[startLeft++]
        else nums[curr++] = aux[startRight++]
    }
    
    
        while(startLeft <= endLeft){
            nums[curr++] = aux[startLeft++]
    }
    
        while(startRight <= endRight){
           nums[curr++] = aux[startRight++]
    }


}
