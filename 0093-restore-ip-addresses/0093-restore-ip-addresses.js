/**
 * @param {string} s
 * @return {string[]}
 */


function isValid(s){
    if(s.length > 3 || s.length < 1) return false
    if(s.length > 1 && s[0] === "0") return false
    if(parseFloat(s) > 255 ||  parseFloat(s) < 0) return false
    return true
}
var restoreIpAddresses = function(s) {
    let res = []
    helper(s, res , 4, [], 0)
    return res
};


function helper(s, res, k , curr, idx){
    if(k === 0  )
    {   if(s.length === idx)
        res.push(curr.join("."))        
        return 
    }
    for(let i = 1 ; i <= Math.min(s.length, 3); i++){
        
        let str = s.slice(idx , idx + i);
        if(isValid(str)){
            curr.push(str)
            helper(s , res, k - 1, curr , idx + i)
            curr.pop()
        }
    }
        
}