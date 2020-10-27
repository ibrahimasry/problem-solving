leetcode 559. Maximum Depth of N-ary Tree// leetcode 559. Maximum Depth of N-ary Tree
// Given a n-ary tree, find its maximum depth.

// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

// Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node} root
 * @return {number}
 */
const maxDepth = function (root) {
  if (!root) return 0;
  let max = 0;

  for (let child of root.children) {
    let res = maxDepth(child);
    max = Math.max(max, res);
  }

  return max + 1;
};
