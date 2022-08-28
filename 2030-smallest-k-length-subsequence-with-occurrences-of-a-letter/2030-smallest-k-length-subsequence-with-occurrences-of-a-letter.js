/**
 * @param {string} s
 * @param {number} k
 * @param {character} letter
 * @param {number} repetition
 * @return {string}
 */
var smallestSubsequence = function(s, k, letter, repetition) {
    
    const last = (arr) => arr[arr.length -1]
    //curr count in stack for the target letter
    //curr count in remaining str for the target curr
    
    // curr remianin length
    let countInStr = s.split("").reduce((a, b) => a + (b ==letter ? 1 : 0), 0)
    let countInStack = 0
    let stack = []
    for(let i =0; i< s.length; i++){
        let currLetter = s[i]
        while(stack.length > 0 && s.length - i + stack.length - 1 >= k   && 
               ((currLetter < last(stack) && (last(stack) != letter || countInStack + countInStr - 1  >= repetition))
                     || k - stack.length < repetition - countInStack))
               
      {
            
            countInStack -= last(stack) == letter ? 1 : 0 
            stack.pop()
        }
            
        if(stack.length < k){
             countInStack = countInStack +  (currLetter === letter ? 1 : 0)
             stack.push(currLetter)
        }
        countInStr -= currLetter == letter ? 1 : 0 


        
    }
    return stack.join("")
    
};