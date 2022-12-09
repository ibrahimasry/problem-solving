# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        def dfs(node, minV, maxV):
            nonlocal res
            if not node :
                res = max(abs(minV-maxV), res)
                return
            dfs(node.left, min(minV, node.val), max(maxV, node.val))
            dfs(node.right, min(minV, node.val), max(maxV, node.val))
        dfs(root, root.val, root.val)
        return res