const insertIntoBST = function (root, val) {
  if (!root) return new TreeNode(val);
  let prev = null;
  let res = root;
  while (root) {
    prev = root;
    if (root.val > val) root = root.left;
    else root = root.right;
  }

  if (prev.val > val) prev.left = new TreeNode(val);
  else prev.right = new TreeNode(val);
  return res;
};
