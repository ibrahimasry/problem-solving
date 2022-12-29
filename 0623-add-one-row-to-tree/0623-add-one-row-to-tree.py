# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if not root :
            return root
        if depth == 1:
            return TreeNode(val,root)
        def dfs(root, d):
            if not root:
                return
            left = dfs(root.left,d-1)
            right = dfs(root.right, d-1)
            if d == 2:
                root.left = TreeNode(val,left)
                root.right = TreeNode(val, None,right)
            return root
        return dfs(root, depth)