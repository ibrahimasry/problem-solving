# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root, curr):
            nonlocal res
            if not root:
                return
            if not root.left and not root.right:
                res += curr * 10 + root.val
                return
            dfs(root.left, curr * 10 + root.val)
            dfs(root.right, curr*10 + root.val)
        dfs(root, 0)
        return res 