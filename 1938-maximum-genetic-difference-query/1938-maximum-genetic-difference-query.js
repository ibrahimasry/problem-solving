/**
 * @param {number[]} parents
 * @param {number[][]} queries
 * @return {number[]}
 */
var maxGeneticDifference = function(parents, queries) {
    
    
     const tri = {count : 0, children : {}}
     const tree = {}
     const ans = []
     const queriesPerNode = {}
     
     for(let i = 0; i < queries.length; i++){
         const [node, val] = queries[i]
         if(queriesPerNode[node] === undefined)
             queriesPerNode[node] = []
         queriesPerNode[node].push([i, val])
         
     }
     function update(num, val){
         let curr = tri
         
         for(let i = 17; i >= 0; i--){
             let bit = (num >> i) & 1 
             
             if( curr.children[bit] === undefined)
                 curr.children[bit] = {count : 0, children : {}}
             curr = curr.children[bit]
             curr.count += val

             
         }
     }
   function query(num){
         let curr = tri
         let ans = 0
         for(let i = 17; i >= 0; i--){
             let bit = (num >> i) & 1 ^ 1
             if( curr.children[bit]  !== undefined && curr.children[bit].count > 0){
                 ans += (1 << i)
                 curr = curr.children[bit]
             }
             else {
                 curr = curr.children[bit ^ 1]
             }
             
         }
       return ans
     }
    
    
    function dfs(node){
         update(node, 1)
        for(let [idx, val] of queriesPerNode[node] || [])
            ans[idx] = query(val)
        
        for(let child of tree[+node] || [])
            dfs(child)
        update(node, -1)
    }
    
    let root = null
    for(let [node, parent] of Object.entries(parents)){
        if(parent === -1)
            root = node
        if(tree[parent] === undefined)
            tree[parent] = []
        tree[parent].push(node)
    }
    dfs(root)
    return ans
    
};