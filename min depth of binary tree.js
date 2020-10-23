// leetcode 111. Minimum Depth of Binary Tree
// Given a binary tree, find its minimum depth.

// The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

// Note: A leaf is a node with no children.

const minDepth = function (root) {
  if (!root) return 0;
  return helper(root);
};

function helper(root) {
  if (!root) return Infinity;
  if (!root.left && !root.right) return 1;

  return Math.min(helper(root.left), helper(root.right)) + 1;
}
