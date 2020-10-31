// Recover Binary Search Tree

// You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

// Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

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
 * @return {void} Do not return anything, modify root in-place instead.
 */
const recoverTree = function (root) {
  let node1,
    node2,
    prev = new TreeNode(-Infinity);

  const helper = (root) => {
    if (!root) return;
    helper(root.left);
    if (root.val < prev.val) {
      if (!node1) node1 = prev;
      node2 = root;
    }
    prev = root;
    helper(root.right);
  };

  helper(root);
  let temp = node1.val;
  node1.val = node2.val;
  node2.val = temp;
};
