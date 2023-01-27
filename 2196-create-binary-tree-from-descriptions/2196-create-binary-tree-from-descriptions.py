/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[][]} descriptions
 * @return {TreeNode}
 */
var createBinaryTree = function(descriptions) {
        const nodes = {}
        const seen = new Set(descriptions.map(curr => curr[0]))
        for (const [node , child , isLeft] of descriptions){
            if (seen.has(child)) seen.delete(child)
            nodes[child] = nodes[child] || new TreeNode(child)
            nodes[node] = nodes[node] || new TreeNode(node)
            if (isLeft == 1)
                nodes[node].left = nodes[child]
            else 
                nodes[node].right = nodes[child]
        }
        return nodes[Array.from(seen)[0]]

    
};