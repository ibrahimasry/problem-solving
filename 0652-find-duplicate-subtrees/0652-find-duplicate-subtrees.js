/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function(root) {
    
    
    let set = {}
    
    helper(root,  set)
    return Object.values(set).filter( root => root !== null)
    
};


function helper(root,  set){
    if(root === null) return null
    
    const val = root.val
    const left = helper(root.left,  set)
    const right = helper(root.right , set)
    
    const str = val + "-" + left + "-" + right
    
    if(str in set) set[str] = root
    else set[str] = null
    return str

}
