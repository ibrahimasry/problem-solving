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
 * @return {number}
 */
var maxProduct = function(root) {
    if(!root) return 0
    
    sum(root)
    return max(root, root.sum) % (10**9 + 7)
    
};

function sum(root){
    if(!root) return 0
  root.sum = sum(root.left)  + sum(root.right) + root.val
    return  root.sum
}


function max(root, overAll){
    if(!root || (!root.left && !root.right)) return 0
    const left =  max(root.left,  overAll)
    const right =  max(root.right, overAll)
    let splitR = root.left ? (overAll - root.left.sum) * root.left.sum : 0
    let splitL = root.right ? (overAll - root.right.sum) * root.right.sum : 0
    
    
   const local = Math.max(splitR, splitL)
   
   
   return Math.max(right, left, local)

}











