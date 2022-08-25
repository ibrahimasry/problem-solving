/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var waysToPartition = function(nums, k) {
    
    let leftCounter = {}
    let rightCounter = {}
    
    function getValue(obj, val) {
        if(obj[val] !== undefined) return obj[val]
        return 0
    }
    
    function addOne(obj, val){
        obj[val] = obj[val] || 0
        obj[val]++ 
        
    }
    
    function minusOne(obj, val){
        obj[val]-- 

        
    }
    let prefix = [...nums]
    
    for(let i  = 1; i < nums.length; i++){
        prefix[i] += prefix[i-1]
    }
    
    for(let i = 1; i < nums.length; i++){
        let diff = prefix[i-1] - (prefix[prefix.length -1] - prefix[i-1])
        addOne(rightCounter, diff)
    }
    
    
    let res = getValue(rightCounter, 0)
    
    
    for(let i = 0; i<nums.length; i++){
        let diff = k - nums[i]
        
        res = Math.max(getValue(rightCounter, -diff) + getValue(leftCounter, diff), res)
        let leftDiff = prefix[i] - (prefix[prefix.length-1] - prefix[i] )
        addOne(leftCounter, leftDiff)
        minusOne(rightCounter, leftDiff)

    }
    return res
    
};