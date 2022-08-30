/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var longestSubsequenceRepeatedK = function(s, k) {
    function isSubsequence(s, curr){
        let i = 0
            for(let j = 0; j < s.length; j++){
                if(s[j] == curr[i])
                    i++
                if(i === curr.length)
                    return true
                    
        }
        return false
    }
    
    let counter = {}
    for(let c of s)
        counter[c] = counter[c] ? ++counter[c] : 1
    let allowed = {}
    for(let [c, count] of Object.entries(counter)){
        if(count >= k){
            allowed[c] = Math.floor(count/k)
        }
    }
    const sortedLetter = Object.keys(allowed).sort((a, b) => b > a ? 1 : -1)
    let cand = []
    
    for(let c of sortedLetter)
        cand.push([c, {[c]:1}])
    while (true){
        const newCand = []
        for(let [c, cnt] of cand){
            for(let curr of sortedLetter){
                if(cnt[curr] === undefined ||  allowed[curr] > cnt[curr]){
                    if(isSubsequence(s, (c + curr).repeat(k))){
                        const newCnt = {...cnt}
                        newCnt[curr] =  newCnt[curr] || 0
                        newCnt[curr]++
                        newCand.push([c+curr, newCnt])
                    }
                    
                }
            }
        }
        
        
        
        if(newCand.length == 0)
            break
            cand = newCand
        
    }
    
    return cand.length > 0 ? cand[0][0] : ""
    
    
};