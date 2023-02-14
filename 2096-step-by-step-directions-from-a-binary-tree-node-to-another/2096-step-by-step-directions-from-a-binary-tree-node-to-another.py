# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path1 = []
        path2 = []
        
        def dfs(node):
            nonlocal path1
            nonlocal path2
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 1:
                path2.append('L')
            if right == 1:
                path2.append('R')
            if left == 2 or right == 2:
                path1.append('U')
            if left + right == 3:
                return 4
            if node.val == startValue:
                return 2 + left + right
            if node.val == destValue:
                return 1 + left + right


            return left + right
        dfs(root)
        return "".join(path1 + path2[::-1])