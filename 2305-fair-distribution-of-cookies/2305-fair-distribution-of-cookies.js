/**
 * @param {number[]} cookies
 * @param {number} k
 * @return {number}
 */
var distributeCookies = function(cookies, k) {
    
    const  arr = Array(k).fill(0)
    const n = (cookies.length)
    let ans = cookies.reduce((a, b) => a+b ,0)
    
    const recurse = (i) => {
        if (i == n){
            ans = Math.min(ans, Math.max(...arr))
            
            return 
        }
        
        for (let j=0; j < k; j++){
            arr[j] += cookies[i]
            recurse(i+1)
            arr[j] -= cookies[i]
        }
    }
    recurse(0)
    return ans
    
};