/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    const seen = new Set(words)
    const dfs = (word)=>{
        for(let i = 0; i < word.length; i++)
            if (seen.has(word.slice(0,i+1)) && dfs(word.slice(i+1)))
                return true
        return word.length === 0
    
    }
    const ans = []
    for(let word of words){
        seen.delete(word)
        if(dfs(word))
            ans.push(word)
        seen.add(word)
    }
    return ans
};