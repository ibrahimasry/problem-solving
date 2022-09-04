/**
 * @param {number[]} parents
 * @param {number[]} nums
 * @return {number[]}
 */
var smallestMissingValueSubtree = function(parents, nums) {
    
    
    const tree = buildTree(parents)
    let currNode = nums.indexOf(1)
    let res = Array(nums.length).fill(1)
    let currSmall = 1
    let visited = Array(Math.max(...nums) * 2).fill(false) 
    while(currNode !== -1){
        dfs(currNode, visited, tree, nums)
        while(visited[currSmall])
            currSmall++
        res[currNode] = currSmall
        currNode = parents[currNode]
        
    }
    return res
};



function buildTree(parents){
    let tree = {}
    for(let [node, parent] of Object.entries(parents)){
        tree[parent] = tree[parent] || []
        tree[parent].push(node)
    }
    return tree
}


function dfs(node, visited, tree, nums){
        if(visited[nums[node]])return
        visited[nums[node]] = true
    for(let child of tree[node] || [])
        {
            dfs(child, visited, tree, nums)
        }
}