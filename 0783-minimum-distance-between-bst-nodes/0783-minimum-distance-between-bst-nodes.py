# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        res = inf
        def dfs(node):
            nonlocal res
            nonlocal prev
            if not node :
                return
            dfs(node.left)
            if prev != None:
                res = min(res, abs(prev - node.val))
            prev = node.val
            dfs(node.right)
        dfs(root)
        return res