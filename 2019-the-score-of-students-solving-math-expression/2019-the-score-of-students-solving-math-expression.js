/**
 * @param {string} s
 * @param {number[]} answers
 * @return {number}
 */
var scoreOfStudents = function(s, answers) {
    const cache = {}
    const wrongResult = getWrongRes(s, 0, s.length , cache)
    let res = 0
    
    let correct = eval(s)
    for(let i =0; i< answers.length; i++)
        if(answers[i] == correct )
            res += 5
         else if (wrongResult.includes(answers[i]))
             res += 2
    
    return res
    
};






function getWrongRes(s, start ,end ,cache){
    if(start == end -1)
        return [+s[start]]
    if( cache[`${start}-${end}`] !== undefined)
        return  cache[`${start}-${end}`]
    
    
    let res = []
    
    for(let i = start+1; i < end; i+=2){
        const curr= s[i]
        if(curr == "+" || curr == "*"){
        let left = getWrongRes(s, start, i, cache)
        let right = getWrongRes(s, i+1, end, cache)
        for(let n of left){
            for(let m of right){
                const x = curr == "+" ? n + m : n*m
                 if(x <= 1000)
                 res.push(x)
            }
        }    
    }
    }
    
    res.push(eval(s.slice(start, end)))
    
    cache[`${start}-${end}`] = new Set(res)
    return res
        
}