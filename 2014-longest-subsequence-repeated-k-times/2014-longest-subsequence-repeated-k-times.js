/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var longestSubsequenceRepeatedK = function(s, k) {
    function isSubsequence(s, sub , k){
            let i = 0
            for(let j = 0; j < s.length; j++){
                if(s[j] == sub[i])
                    i++
                if(i === sub.length && k == 1)
                    return true
                if(i === sub.length){
                    i=0
                    k--
                }
                    
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
        for(let [sub, cnt] of cand){
            for(let curr of sortedLetter){
                if(cnt[curr] === undefined ||  allowed[curr] > cnt[curr]){
                    if(isSubsequence(s, (sub + curr), k)){
                        newCand.push([sub+curr, {...cnt, [curr] : cnt[curr] ? cnt[curr] + 1 : 1}])
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