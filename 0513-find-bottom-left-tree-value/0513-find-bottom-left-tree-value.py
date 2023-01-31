# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        depth = -1
        res = -1
        
        def dfs(node,d):
            nonlocal depth
            nonlocal res
            if not node:
                return
            if node.left == None and node.right == None:
                if d > depth:
                    depth = d
                    res = node.val
            dfs(node.left, d+1)
            dfs(node.right,d+1)
        dfs(root, 0)
        return res