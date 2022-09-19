/**
 * @param {string[][]} paths
 * @return {string[][]}
 */
var deleteDuplicateFolder = function(paths) {
    
    
    const tri = buildTri(paths).root
    const hash = {}
    dfs(tri , hash)
    for(let key of Object.keys(hash)){
        if(hash[key].length > 1)
            for(let node of hash[key])
                node.isDelete = true
    }

    
    const res = []
    deleteDup(tri, res , "")
    
   return  res.map(arr=> {
        arr.shift()
        return arr  
     })
    
};

function deleteDup(tri, res , curr){
    if(!tri) return
    for(let child  of Object.keys(tri)){
        if(!tri[child])
            continue
        if(!(tri[child].isDelete))
            deleteDup(tri[child], res, curr + "," + child)
        
    }
    
    if(curr?.length)
        res.push(curr.split(","))
    
}

function dfs(tri, hash){
    if(!tri) return "()"
    let ans = "("
    for(let child  of Object.keys(tri).sort()){
       ans += child +  dfs(tri[child], hash)   
    }
    
    ans += ")"
    
    if(ans !== "()"){
        hash[ans] = hash[ans] || []
        hash[ans].push(tri)
    }
    return ans
}

function buildTri(paths){
    
    const tri = new Tri()
    for(let path of paths)
        tri.insert(path)
    
    return tri
    
}


class Tri {
    
    root = {}

    insert = (path) =>
    {
        let curr = this.root
        for(let c of path){
            if(c in curr){
                curr = curr[c]
            }
            else {
                curr[c] = {}
                curr = curr[c]
            }
        }
    }
}