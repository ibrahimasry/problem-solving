/**
 * @param {string} stamp
 * @param {string} target
 * @return {number[]}
 */
var movesToStamp = function(stamp, target) {
    
    
    let res = []
    let remain = target.length
    target = target.split("")
    
    function check(start){
        
        let flag = false
        for(let i = start; i< start + stamp.length; i++){
            if(target[i] == "?") continue
            if(target[i] !== stamp[i-start]) return false
            flag = true
        }
        
        return flag
        
        
    }
    
    function update(start){

     for(let i = start; i < start + stamp.length; i++){
         if(target[i] !== "?") {
           target[i] = "?"
            remain--
         }
     }
    }
    while (remain > 0){
        
        let flag = false
        for(let i = 0; i < target.length-stamp.length + 1; i++){
            
            if(check(i))
            {
                update(i)
                res.push(i)   
                flag = true
            }
            if(flag)
                break
                
        }
        if(!flag) return []
        
        
    }
    
    return res.reverse()
};