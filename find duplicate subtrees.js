// leetcode 652. Find Duplicate Subtrees
// Given the root of a binary tree, return all duplicate subtrees.

// For each kind of duplicate subtrees, you only need to return the root node of any one of them.

// Two trees are duplicate if they have the same structure with the same node values.

const findDuplicateSubtrees = function (root) {
  const set = {};
  const res = [];

  const helper = (root) => {
    if (!root) return "#";
    let curr = root.val + "," + helper(root.left) + "," + helper(root.right);
    if (set[curr] === 1) res.push(root);
    set[curr] = set[curr] ? ++set[curr] : 1;
    return curr;
  };
  helper(root);
  return res;
};
