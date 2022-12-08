# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def dfs(node, arr):
            
            if not node:
                return
            if not node.left and not node.right:
                arr.append(node.val)
            dfs(node.left,arr)
            dfs(node.right, arr)
            
        dfs(root1, arr1)
        dfs(root2, arr2)
        if len(arr1) != len(arr2):
            return False
        for i, v in enumerate(arr1):
            if v != arr2[i]:
                return False
        return True