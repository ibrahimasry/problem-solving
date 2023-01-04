# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return
            if node.val != root.val:
                return node.val
            if node.left:
                return min(dfs(node.left), dfs(node.right))
            
            return inf
        res = dfs(root)
        
        if res == inf:
            return -1
        return res