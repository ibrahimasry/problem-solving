# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        
        
        def dfs(node):
            if not node:
                return (0,0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            case0 = left[1] + right[1]
            if not node.left and not node.right:
                case1 = 1
            elif not node.left:
                case1 = right[2]
            elif not node.right:
                case1 = left[2]
            else:
                case1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
            case2 = 1 + min(left) + min(right)
            return (case0,case1, case2)
        return min(dfs(root)[1:])