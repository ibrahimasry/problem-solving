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
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            curr = 1 if node.val == destValue else 0
            curr = 2 if node.val == startValue else curr
            #found the dist so we get down to it by left and right
            if left == 1 or right == 1:
                path2.append('L' if left == 1 else "R")
                
            #found the start so we go up till we find the lca
            if left == 2 or right == 2:
                path1.append('U')
            #we find the lca then reset and dont add any dirs
            if left + right + curr == 3:
                return 0
            return left + right + curr
        dfs(root)
        return "".join(path1 + path2[::-1])