/**
 * @param {number[]} heights
 * @return {number[]}
 */
var canSeePersonsCount = function(heights) {
    
    
    const res = []
    const stack = []
    for(let i = heights.length - 1; i >=0; i--){
        let curr = heights[i]
        let size = 0
        
        while(stack.length && stack[stack.length - 1] <= curr){
            size++
            stack.pop()
        }
        
        if(stack.length)
            size++
         stack.push(curr)
        res.push(size)
    }
    
    return res.reverse()
    
};