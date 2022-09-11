/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    
    const ans = []
    const dp = []
    
    
    for (let c of obstacles){
        let index = bisectRight(dp, c)
        if(index >= dp.length)
            dp.push(c)
        else dp[index] = c
        ans.push(index + 1)
    }
    return ans
    
};


function bisectRight(arr, target){
    let l =0
    let h = arr.length - 1
    while(l < h){
        let m = Math.ceil((l+h) / 2)
        if(arr[m] <= target)
            l = m 
        else h= m -1
    }
    
    return arr[l] <= target ?  l + 1 : l
}